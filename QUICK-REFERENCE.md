# ⚡ Git 敏感信息泄露 - 快速修复参考

## 🚨 紧急三步走

### 1️⃣ 立即轮换密钥
```
⚠️ 最重要！在清理历史之前必须先轮换密钥
```

### 2️⃣ 清理历史并推送

**方案 A：完全清除（最简单）**
```bash
rm -rf .git
git init && git branch -M main
git add . && git commit -m "Initial commit - cleared all history"
git remote add origin <URL>
git push -f origin main
```

**方案 B：替换敏感信息（保留历史）**
```bash
pip install git-filter-repo
cat > replacements.txt << EOF
旧密钥==>REDACTED
EOF
git filter-repo --replace-text replacements.txt --force
git push origin --force --all
```

### 3️⃣ 通知团队成员
```bash
# 团队成员执行：
git fetch origin && git reset --hard origin/main
```

---

## 🛡️ 预防措施

### 安装 git-secrets
```bash
brew install git-secrets
git secrets --install
git secrets --add 'your-pattern'
```

### 使用环境变量
```python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
```

### .gitignore 配置
```
.env
.env.local
*.key
*.pem
```

---

## ✅ 检查清单

- [ ] 轮换密钥
- [ ] 清理历史
- [ ] 强制推送
- [ ] 通知团队
- [ ] 安装 git-secrets
- [ ] 使用环境变量

---

详细指南请查看：`SECURITY-FIX-GUIDE.md`

