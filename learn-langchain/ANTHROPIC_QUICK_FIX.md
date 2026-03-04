# 🚀 Anthropic Agent - 快速修复指南

## ⚠️ 问题说明

你遇到的导入错误：
```
ImportError: cannot import name 'AgentExecutor' from 'langchain.agents'
```

**原因**: LangChain 0.3+ 版本弃用了旧的 Agent API（`AgentExecutor`, `create_react_agent`）

## ✅ 解决方案

我已经创建了**三个版本**，按推荐度排序：

### 🥇 方案 1: 最简单版本（强烈推荐）⭐⭐⭐

**文件**: `use-agent-anthropic-simple.py`

**特点**:
- ✅ 不使用任何已弃用的 API
- ✅ 代码最简单，最稳定
- ✅ 支持单次问答和多轮对话
- ✅ 无需额外安装依赖

**运行**:
```bash
python use-agent-anthropic-simple.py
```

---

### 🥈 方案 2: 纯问答版本 ⭐⭐⭐

**文件**: `use-agent-anthropic-qa-only.py`

**特点**:
- ✅ 更详细的示例代码
- ✅ 包含函数封装
- ✅ 适合学习和二次开发

**运行**:
```bash
python use-agent-anthropic-qa-only.py
```

---

### 🥉 方案 3: LangGraph 版本（需要额外安装）⭐⭐

**文件**: `use-agent-anthropic-langgraph.py`

**特点**:
- ✅ 使用最新的 LangGraph 框架
- ✅ 支持工具调用（计算器示例）
- ✅ 更强大的 Agent 能力
- ⚠️ 需要安装 `langgraph`

**安装依赖**:
```bash
pip install langgraph
```

**运行**:
```bash
python use-agent-anthropic-langgraph.py
```

---

## 📦 所需依赖

### 方案 1 和 2（推荐）
```bash
pip install langchain-anthropic python-dotenv
```

### 方案 3（可选）
```bash
pip install langchain-anthropic python-dotenv langgraph
```

---

## ⚙️ 环境配置

在项目根目录创建 `.env` 文件：

```bash
# 必需
ANTHROPIC_API_KEY=sk-ant-your-key-here

# 可选（使用代理或自定义端点）
ANTHROPIC_BASE_URL=https://api.anthropic.com

# 可选（指定模型）
ANTHROPIC_MODEL_NAME=claude-3-5-sonnet-20241022
```

---

## 🎯 快速开始

### 步骤 1: 选择方案

**如果你不确定选哪个** → 使用方案 1（`use-agent-anthropic-simple.py`）

### 步骤 2: 配置 API Key

```bash
echo "ANTHROPIC_API_KEY=sk-ant-your-actual-key" > .env
```

### 步骤 3: 运行

```bash
# 方案 1 - 最简单（推荐）
python use-agent-anthropic-simple.py

# 或方案 2 - 纯问答
python use-agent-anthropic-qa-only.py

# 或方案 3 - LangGraph（需先安装 langgraph）
pip install langgraph  # 首次运行需要
python use-agent-anthropic-langgraph.py
```

---

## 📊 三个方案对比

| 特性 | 方案 1 (simple) | 方案 2 (qa-only) | 方案 3 (langgraph) |
|------|----------------|------------------|-------------------|
| 代码复杂度 | ⭐ 简单 | ⭐ 简单 | ⭐⭐⭐ 较复杂 |
| 依赖数量 | 少 | 少 | 多（需 langgraph）|
| 稳定性 | ⭐⭐⭐ 最稳定 | ⭐⭐⭐ 最稳定 | ⭐⭐ 较稳定 |
| 工具支持 | ❌ 无 | ❌ 无 | ✅ 有 |
| 多轮对话 | ✅ 支持 | ✅ 支持 | ✅ 支持 |
| 推荐度 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

---

## 💡 代码示例

### 方案 1 和 2 的使用方式

```python
from use_agent_anthropic_simple import chat

# 简单问答
answer = chat("什么是 Python？")
print(answer)
```

### 方案 3 的使用方式（带工具）

```python
from use_agent_anthropic_langgraph import chat

# 会自动使用计算器工具
answer = chat("计算 123 + 456")
print(answer)
```

---

## 🔧 故障排查

### 问题 1: 缺少 `langchain_anthropic` 模块

```bash
pip install langchain-anthropic
```

### 问题 2: 缺少 `langgraph` 模块（仅方案 3）

```bash
pip install langgraph
```

### 问题 3: API Key 错误

确保 `.env` 文件在项目根目录，且格式正确：
```bash
ANTHROPIC_API_KEY=sk-ant-api03-...
```

### 问题 4: 网络连接问题

在 `.env` 中添加代理地址：
```bash
ANTHROPIC_BASE_URL=https://your-proxy-url.com/v1
```

---

## 🎓 学习建议

1. **新手**: 从方案 1 开始（`use-agent-anthropic-simple.py`）
2. **需要工具**: 学习方案 3（`use-agent-anthropic-langgraph.py`）
3. **生产环境**: 使用方案 1 或 2（更稳定）

---

## 📚 相关文档

- `QUICKSTART_ANTHROPIC.md` - 3 分钟快速开始
- `ANTHROPIC_AGENT_README.md` - 完整使用文档
- `ENV_CONFIG_GUIDE.md` - 环境配置详解
- `ANTHROPIC_FIX_NOTES.md` - 修复说明

---

## ✅ 测试验证

运行测试文件验证配置：

```bash
python test-anthropic-agent.py
```

---

**最后更新**: 2026-02-10  
**推荐**: 使用方案 1 (`use-agent-anthropic-simple.py`) 🚀

