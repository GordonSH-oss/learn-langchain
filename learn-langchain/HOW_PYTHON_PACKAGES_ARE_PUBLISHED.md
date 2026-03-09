# Python 项目如何发布到 PyPI

> 从源代码到 `pip install` 的完整流程解析

## 🎯 核心问题

**问题**: LangChain 的源代码是怎么发布的，才能让我们通过 `pip install langchain` 安装使用？

**答案**: 通过 **PyPI (Python Package Index)** 这个 Python 的官方包仓库！

---

## 📦 完整发布流程

```
源代码 → 打包配置 → 构建包 → 上传到 PyPI → pip install
```

让我们逐步解析每个环节：

---

## 1️⃣ 源代码组织

### LangChain 的项目结构

```
langchain/                          # GitHub 仓库根目录
├── libs/                          # 所有子包都在这里
│   ├── langchain/                 # 主包（langchain-classic）
│   │   ├── langchain/            # 源代码目录
│   │   │   ├── __init__.py
│   │   │   ├── agents/
│   │   │   ├── chains/
│   │   │   └── ...
│   │   ├── pyproject.toml        # 📦 打包配置文件（重要！）
│   │   ├── README.md
│   │   └── tests/
│   │
│   ├── core/                      # langchain-core 包
│   │   ├── langchain_core/       # 源代码
│   │   ├── pyproject.toml        # 📦 打包配置
│   │   └── ...
│   │
│   ├── partners/                  # 各种集成包
│   │   ├── anthropic/            # langchain-anthropic
│   │   │   ├── langchain_anthropic/
│   │   │   └── pyproject.toml
│   │   ├── openai/               # langchain-openai
│   │   └── ...
│   │
│   └── text-splitters/           # langchain-text-splitters
│       └── pyproject.toml
│
├── .github/                       # GitHub Actions（自动化）
│   └── workflows/
│       └── release.yml           # 自动发布流程
│
└── README.md
```

---

## 2️⃣ 打包配置文件：pyproject.toml

这是关键！`pyproject.toml` 告诉 Python 如何打包这个项目。

### 示例：LangChain 的 pyproject.toml

```toml
[build-system]
requires = ["hatchling"]              # 使用的构建工具
build-backend = "hatchling.build"

[project]
name = "langchain-classic"            # 📦 包名（pip install 时用的名字）
version = "1.0.2"                     # 版本号
description = "Building applications with LLMs through composability"
license = { text = "MIT" }
readme = "README.md"
requires-python = ">=3.10.0,<4.0.0"   # Python 版本要求

# 依赖项（安装这个包时会自动安装这些依赖）
dependencies = [
    "langchain-core>=1.2.17,<2.0.0",
    "langchain-text-splitters>=1.1.0,<2.0.0",
    "pydantic>=2.7.4,<3.0.0",
    "requests>=2.0.0,<3.0.0",
]

# 可选依赖（pip install langchain[openai]）
[project.optional-dependencies]
anthropic = ["langchain-anthropic"]
openai = ["langchain-openai"]

# 项目链接
[project.urls]
Homepage = "https://docs.langchain.com/"
Repository = "https://github.com/langchain-ai/langchain"
```

### pyproject.toml 的关键配置

| 配置项 | 作用 | 示例 |
|--------|------|------|
| `name` | PyPI 上的包名 | `langchain-classic` |
| `version` | 版本号 | `1.0.2` |
| `dependencies` | 必需的依赖 | `["pydantic>=2.7.4"]` |
| `optional-dependencies` | 可选功能 | `anthropic = ["langchain-anthropic"]` |
| `requires-python` | Python 版本要求 | `">=3.10.0"` |

---

## 3️⃣ 构建 Python 包

### 使用构建工具打包

```bash
# 进入包目录
cd langchain/libs/langchain

# 方法 1: 使用 build 工具（推荐）
pip install build
python -m build

# 方法 2: 使用 hatchling（LangChain 使用的）
pip install hatchling
hatchling build

# 方法 3: 使用 setuptools（传统方式）
python setup.py sdist bdist_wheel
```

### 构建结果

构建后会生成 `dist/` 目录：

```
dist/
├── langchain_classic-1.0.2-py3-none-any.whl  # Wheel 包（推荐）
└── langchain_classic-1.0.2.tar.gz            # 源代码压缩包
```

**两种包格式**：
- **`.whl` (Wheel)**: 预编译的二进制包，安装更快（推荐）
- **`.tar.gz` (Source Distribution)**: 源代码包，需要在安装时编译

---

## 4️⃣ 上传到 PyPI

### 手动上传（使用 twine）

```bash
# 1. 安装 twine
pip install twine

# 2. 上传到 PyPI
twine upload dist/*

# 或者先上传到 TestPyPI 测试
twine upload --repository testpypi dist/*
```

### 自动上传（GitHub Actions）

LangChain 使用 GitHub Actions 自动发布，当打新 tag 时自动触发：

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'langchain-classic==*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install build twine
      
      - name: Build package
        run: python -m build
      
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

### PyPI 认证

需要在 PyPI 上注册账号并获取 API Token：

1. 注册 PyPI 账号: https://pypi.org/account/register/
2. 生成 API Token: https://pypi.org/manage/account/token/
3. 配置到 GitHub Secrets 或本地 `~/.pypirc`

---

## 5️⃣ 用户安装使用

一旦上传到 PyPI，用户就可以安装了：

```bash
# 基础安装
pip install langchain-classic

# 安装特定版本
pip install langchain-classic==1.0.2

# 安装可选依赖
pip install langchain-classic[anthropic,openai]

# 升级到最新版本
pip install --upgrade langchain-classic
```

### pip install 背后发生了什么？

1. **查询 PyPI**: pip 连接到 https://pypi.org/pypi/langchain-classic/json
2. **下载包**: 下载 `.whl` 或 `.tar.gz` 文件
3. **解析依赖**: 读取 `pyproject.toml` 中的 `dependencies`
4. **安装依赖**: 递归安装所有依赖包
5. **安装包**: 将包复制到 `site-packages/` 目录

---

## 🔧 实际案例：LangChain 的发布流程

### 1. 开发者更新代码

```bash
# 在 libs/langchain/ 目录下修改代码
vim langchain/agents/create_agent.py

# 提交代码
git add .
git commit -m "Add new feature to create_agent"
git push origin main
```

### 2. 更新版本号

```toml
# 修改 libs/langchain/pyproject.toml
[project]
version = "1.0.3"  # 从 1.0.2 升级到 1.0.3
```

### 3. 打 Git Tag

```bash
# 创建版本标签
git tag langchain-classic==1.0.3
git push origin langchain-classic==1.0.3
```

### 4. 自动触发 GitHub Actions

- GitHub Actions 检测到新 tag
- 自动运行测试
- 自动构建包
- 自动上传到 PyPI

### 5. 用户可以安装新版本

```bash
pip install --upgrade langchain-classic
# 现在安装的就是 1.0.3 版本
```

---

## 📊 版本管理

### 语义化版本（Semantic Versioning）

```
MAJOR.MINOR.PATCH
  1  .  0  .  2

1 = 主版本号（不兼容的 API 修改）
0 = 次版本号（向后兼容的功能性新增）
2 = 修订号（向后兼容的问题修正）
```

**示例**：
- `1.0.0` → `1.0.1`: Bug 修复
- `1.0.1` → `1.1.0`: 新增功能，向后兼容
- `1.1.0` → `2.0.0`: 重大更新，可能不兼容

---

## 🌳 Monorepo 结构（LangChain 采用的）

LangChain 是一个 **Monorepo**（单一仓库，多个包）：

```
langchain/                    # 一个 Git 仓库
├── libs/
│   ├── langchain/           → 发布为 langchain-classic
│   ├── core/                → 发布为 langchain-core
│   ├── partners/
│   │   ├── anthropic/       → 发布为 langchain-anthropic
│   │   └── openai/          → 发布为 langchain-openai
│   └── text-splitters/      → 发布为 langchain-text-splitters
```

**优势**：
- ✅ 所有包在同一个仓库，便于管理
- ✅ 可以同时修改多个包
- ✅ 统一的 CI/CD 流程

**每个子包独立发布**：
- 每个子包有自己的 `pyproject.toml`
- 有独立的版本号
- 可以单独发布到 PyPI

---

## 🛠️ 常用构建工具对比

| 工具 | 配置文件 | 特点 | 使用者 |
|------|----------|------|--------|
| **setuptools** | `setup.py` / `setup.cfg` | 传统方式，功能强大 | 早期项目 |
| **hatchling** | `pyproject.toml` | 现代化，简单快速 | LangChain |
| **poetry** | `pyproject.toml` | 依赖管理 + 打包 | 很多新项目 |
| **flit** | `pyproject.toml` | 极简，适合纯 Python 项目 | 小型项目 |
| **PDM** | `pyproject.toml` | PEP 582 支持 | 新兴工具 |

---

## 💡 如何创建自己的 Python 包？

### 最简示例

**1. 项目结构**
```
my_awesome_package/
├── my_awesome_package/
│   ├── __init__.py
│   └── core.py
├── pyproject.toml
└── README.md
```

**2. pyproject.toml**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-awesome-package"
version = "0.1.0"
description = "My awesome Python package"
dependencies = [
    "requests>=2.0.0",
]
```

**3. 构建和发布**
```bash
# 构建
pip install build
python -m build

# 上传到 PyPI
pip install twine
twine upload dist/*
```

**4. 用户安装**
```bash
pip install my-awesome-package
```

---

## 🔗 学习资源

### 官方文档
- **PyPI**: https://pypi.org/
- **Python 打包指南**: https://packaging.python.org/
- **pyproject.toml 规范**: https://peps.python.org/pep-0621/

### LangChain 相关
- **LangChain GitHub**: https://github.com/langchain-ai/langchain
- **LangChain PyPI**: https://pypi.org/project/langchain-classic/
- **发布工作流**: https://github.com/langchain-ai/langchain/blob/main/.github/workflows/

### 工具文档
- **hatchling**: https://hatch.pypa.io/
- **poetry**: https://python-poetry.org/
- **twine**: https://twine.readthedocs.io/

---

## 📝 总结

### Python 包发布流程

```
1. 编写代码 (langchain/agents/)
   ↓
2. 配置 pyproject.toml (定义包名、版本、依赖)
   ↓
3. 构建包 (python -m build → 生成 .whl 和 .tar.gz)
   ↓
4. 上传到 PyPI (twine upload dist/*)
   ↓
5. 用户安装 (pip install langchain-classic)
   ↓
6. 代码被复制到 site-packages/
   ↓
7. 在 Python 中 import langchain 使用
```

### 关键文件
- **`pyproject.toml`**: 定义包的元数据、依赖、构建方式
- **`dist/`**: 构建后的包文件（.whl 和 .tar.gz）
- **`site-packages/`**: pip 安装后的位置

### 核心概念
- **PyPI**: Python Package Index，Python 的官方包仓库
- **pip**: Python 的包管理工具
- **Wheel (.whl)**: 预编译的二进制包，安装快
- **Source Distribution (.tar.gz)**: 源代码包

---

**现在你知道 LangChain 是如何从 GitHub 源代码变成可以 `pip install` 的包了！** 🎉

如果你想深入了解 LangChain 的具体发布流程，可以查看：
- LangChain 的 `.github/workflows/` 目录
- 各个子包的 `pyproject.toml` 配置
- LangChain 的发布文档

有任何问题随时问我！📦✨
