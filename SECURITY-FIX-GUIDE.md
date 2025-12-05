# 🔒 Git 敏感信息泄露修复指南

## 📋 问题场景

当敏感信息（API 密钥、密码、Token 等）被意外提交到 Git 仓库并推送到远程时，需要立即处理。

## 🚨 紧急处理流程

### 第一步：立即轮换密钥（最重要！）

**⚠️ 在清理历史之前，必须先轮换所有泄露的密钥！**

原因：
- 密钥可能已经被克隆
- GitHub/GitLab 可能有缓存
- CI/CD 可能已经使用过
- 恶意扫描器可能已抓取

**操作：**
1. 登录相关平台（API 服务提供商）
2. 立即生成新的 API 密钥
3. 更新 `.env` 文件中的新密钥
4. 删除或禁用旧的密钥

---

### 第二步：清理 Git 历史

#### 方案 A：完全清除历史（最简单，适合新项目）

```bash
# 1. 删除 .git 目录
rm -rf .git

# 2. 重新初始化仓库
git init
git branch -M main

# 3. 添加文件（确保 .env 在 .gitignore 中）
git add .
git commit -m "Initial commit - cleared all history"

# 4. 强制推送到远程
git remote add origin <远程仓库URL>
git push -f origin main
```

**适用场景：**
- 项目刚创建，历史不重要
- 团队成员少，容易协调
- 没有重要的历史记录需要保留

#### 方案 B：使用 git-filter-repo（保留历史，替换敏感信息）

```bash
# 1. 安装工具
pip install git-filter-repo

# 2. 创建替换规则文件
cat > replacements.txt << 'EOF'
旧密钥==>REDACTED_API_KEY
旧密码==>REDACTED_PASSWORD
EOF

# 3. 清理历史
git filter-repo --replace-text replacements.txt --force

# 4. 优化仓库
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 5. 强制推送
git push origin --force --all
git push origin --force --tags
```

**适用场景：**
- 需要保留 Git 历史
- 只需要替换敏感信息
- 项目有重要的提交历史

#### 方案 C：使用 BFG Repo-Cleaner

```bash
# 1. 安装 BFG
brew install bfg

# 2. 创建密码文件
cat > passwords.txt << EOF
旧密钥1
旧密钥2
EOF

# 3. 克隆镜像仓库
cd /tmp
git clone --mirror <仓库URL>
cd <仓库名>.git

# 4. 运行 BFG
bfg --replace-text passwords.txt

# 5. 清理和推送
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

---

### 第三步：更新代码使用环境变量

**确保敏感信息不再硬编码：**

1. **创建 `.env` 文件**（不提交到 Git）
```bash
API_KEY=your-actual-api-key
BASE_URL=your-base-url
```

2. **创建 `.env.example` 文件**（提交到 Git）
```bash
API_KEY=your-api-key
BASE_URL=your-base-url
```

3. **更新代码使用环境变量**
```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
```

4. **更新 `.gitignore`**
```
.env
.env.local
.env.*.local
```

---

### 第四步：通知团队成员

**如果已推送到远程，必须通知团队成员：**

```bash
# 团队成员需要执行：
git fetch origin
git reset --hard origin/main

# 或者重新克隆
git clone <仓库URL>
```

---

## 🛡️ 预防措施

### 1. 安装 git-secrets（推荐）

```bash
# 安装
brew install git-secrets

# 配置
git secrets --install

# 添加自定义模式
git secrets --add 'your-api-key-pattern'
git secrets --add '.*-api-key-.*'
```

### 2. 使用 pre-commit hook

创建 `.git/hooks/pre-commit`：
```bash
#!/bin/bash
# 检查敏感信息
if git diff --cached | grep -E "(api[_-]?key|password|secret|token)" -i > /dev/null; then
    echo "❌ 错误：检测到可能的敏感信息！"
    echo "请使用环境变量而不是硬编码"
    exit 1
fi
```

### 3. 使用 GitHub Secret Scanning

- GitHub 会自动扫描并通知敏感信息泄露
- 在仓库 Settings → Security → Secret scanning 中启用

### 4. 代码审查清单

提交前检查：
- [ ] 没有硬编码的 API 密钥
- [ ] 没有硬编码的密码
- [ ] `.env` 文件在 `.gitignore` 中
- [ ] 使用环境变量读取配置
- [ ] 有 `.env.example` 文件作为模板

---

## 📝 快速检查清单

遇到敏感信息泄露时：

- [ ] **立即轮换密钥**（最重要！）
- [ ] 确认 `.env` 在 `.gitignore` 中
- [ ] 选择清理方案（完全清除 / 替换敏感信息）
- [ ] 执行清理操作
- [ ] 强制推送到远程
- [ ] 通知团队成员同步
- [ ] 安装 git-secrets 防止未来泄露
- [ ] 更新代码使用环境变量

---

## 🔍 验证清理结果

```bash
# 检查是否还有敏感信息
git log --all -p | grep -i "your-sensitive-info"

# 应该没有输出，或者只看到 REDACTED 字样
```

---

## 📚 相关工具和资源

- **git-filter-repo**: https://github.com/newren/git-filter-repo
- **BFG Repo-Cleaner**: https://rtyley.github.io/bfg-repo-cleaner/
- **git-secrets**: https://github.com/awslabs/git-secrets
- **GitHub Secret Scanning**: https://docs.github.com/en/code-security/secret-scanning

---

## 💡 最佳实践

1. **永远不要提交敏感信息**
   - 使用环境变量
   - 使用密钥管理服务（AWS Secrets Manager, HashiCorp Vault 等）

2. **使用 CI/CD 变量**
   - GitHub Secrets
   - GitLab CI/CD Variables
   - 其他平台的 Secret 管理

3. **定期审计**
   - 定期检查 Git 历史
   - 使用自动化工具扫描

4. **最小权限原则**
   - 只给必要的权限
   - 定期轮换密钥

---

## ⚠️ 重要提醒

1. **密钥轮换优先级最高** - 即使清理了历史，也必须轮换密钥
2. **强制推送会影响团队** - 需要协调团队成员
3. **检查 CI/CD 配置** - 确保 CI/CD 中也使用环境变量
4. **检查 Fork 和镜像** - 如果有 Fork，需要联系 Fork 者删除

---

## 📞 需要帮助？

如果遇到问题：
1. 检查是否有推送权限
2. 检查分支保护规则
3. 联系仓库管理员
4. 查看平台文档（GitHub/GitLab 等）

---

**记住：预防胜于治疗！** 从一开始就使用环境变量和密钥管理工具，避免敏感信息泄露。

