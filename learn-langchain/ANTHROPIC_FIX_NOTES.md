# Anthropic Agent 修复说明

## 问题描述

在运行 `use-agent-anthropic-simple.py` 时遇到导入错误：

```
ImportError: cannot import name 'AgentExecutor' from 'langchain.agents'
```

## 原因分析

LangChain 的 API 在不同版本之间有变化。旧的导入方式：
```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
```

在新版本中已经不再支持或路径发生了变化。

## 解决方案

已将代码更新为使用更现代和稳定的 API：

### 修改前
```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
```

### 修改后
```python
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
```

### 主要变化

1. **Agent 创建方式**：
   - 旧：`create_react_agent` (ReAct 模式)
   - 新：`create_tool_calling_agent` (工具调用模式)

2. **Prompt 模板**：
   - 旧：`PromptTemplate.from_template()` (字符串模板)
   - 新：`ChatPromptTemplate.from_messages()` (消息列表模板)

3. **工具定义**：
   - 旧：使用 `Tool` 类包装函数
   - 新：使用 `@tool` 装饰器直接定义

## 兼容性说明

### 当前版本要求

```bash
pip install langchain>=0.1.0 langchain-anthropic>=0.1.0 langchain-core>=0.1.0
```

### 推荐的安装方式

```bash
# 安装最新版本
pip install --upgrade langchain langchain-anthropic langchain-core

# 或者指定版本
pip install langchain>=0.1.0 langchain-anthropic>=1.3.0 langchain-core>=1.2.0
```

## 测试验证

运行以下命令测试修复后的代码：

```bash
# 确保在正确的虚拟环境中
workon langchain-1

# 运行简单问答（推荐）
python use-agent-anthropic-qa-only.py

# 运行带工具的 Agent
python use-agent-anthropic-simple.py

# 运行完整测试
python test-anthropic-agent.py
```

## 两个文件的区别

### 1. `use-agent-anthropic-qa-only.py` ⭐ 推荐
- **特点**：直接使用 ChatAnthropic，无需 Agent 框架
- **优势**：
  - 代码简单，不依赖复杂的 Agent API
  - 版本兼容性好
  - 适合纯问答场景
- **适用场景**：纯对话、不需要工具调用

### 2. `use-agent-anthropic-simple.py`
- **特点**：使用 Agent 框架和工具调用
- **优势**：
  - 可以调用外部工具
  - 自动推理和决策
  - 适合复杂任务
- **适用场景**：需要调用工具、API 或执行复杂操作

## 常见问题

### Q1: 我应该使用哪个文件？

- **新手或简单问答**：使用 `use-agent-anthropic-qa-only.py`
- **需要工具支持**：使用 `use-agent-anthropic-simple.py`

### Q2: 如果还是遇到导入错误怎么办？

```bash
# 1. 更新所有依赖
pip install --upgrade langchain langchain-anthropic langchain-core

# 2. 检查版本
pip show langchain langchain-anthropic langchain-core

# 3. 如果问题持续，重新安装
pip uninstall langchain langchain-anthropic langchain-core
pip install langchain langchain-anthropic langchain-core
```

### Q3: 为什么不使用 ReAct Agent？

`create_react_agent` 在某些版本中可能不稳定或需要额外的配置。`create_tool_calling_agent` 是更现代的方法，直接利用模型的原生工具调用能力。

### Q4: 我的 LangChain 版本太旧怎么办？

如果你必须使用旧版本，建议只使用 `use-agent-anthropic-qa-only.py`，它不依赖 Agent 框架。

## 更新日志

- **2026-02-10**: 修复导入错误，更新为 `create_tool_calling_agent`
- **2026-02-10**: 添加 `ANTHROPIC_BASE_URL` 支持
- **2026-02-10**: 创建测试文件和完整文档

## 相关资源

- [LangChain 迁移指南](https://python.langchain.com/docs/versions/migrating_chains)
- [LangChain Anthropic 集成](https://python.langchain.com/docs/integrations/chat/anthropic)
- [Agent 创建指南](https://python.langchain.com/docs/modules/agents)

---

**提示**: 如果遇到任何问题，优先使用 `use-agent-anthropic-qa-only.py`，它是最稳定和简单的实现。

