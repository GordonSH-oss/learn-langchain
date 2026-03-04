# LangChain & LangGraph 学习项目

> 通过实践学习 LangChain 和 LangGraph 的完整示例集合

## 📁 项目结构

```
learn-langchain/
├── README.md                      # 本文件
├── .env.example                   # 环境变量模板
├── examples/                      # 📚 示例代码
│   ├── use-agent-anthropic-qa-only.py          # ⭐ 最简单：纯问答
│   ├── use-agent-anthropic-simple.py           # ⭐ 推荐：带工具的Agent
│   ├── use-agent-anthropic-langgraph.py        # LangGraph版本
│   ├── use-agent-tool.py                       # 基础工具示例
│   ├── use-agent-tool-real-weather.py          # 真实API集成
│   ├── use-agent-with-memory-1.py              # 记忆系统v1
│   ├── use-agent-with-memory-improved.py       # 记忆系统v2
│   ├── use-agent-with-memory-realistic.py      # ⭐ 生产级记忆
│   ├── test-anthropic-agent.py                 # 测试脚本
│   └── compare-state-fields.py                 # 状态字段对比
├── docs/                          # 📖 文档
│   ├── guides/                    # 使用指南
│   │   ├── ENV_CONFIG_GUIDE.md                # 环境配置指南
│   │   ├── WEATHER_API_GUIDE.md               # 天气API集成
│   │   └── HOW_TO_FILL_USER_INFO.md           # 用户信息管理
│   └── advanced/                  # 进阶文档
│       ├── create-agent-analysis.md           # create_agent源码分析
│       ├── tool-strategy-analysis.md          # ToolStrategy原理
│       └── AGENT_STATE_FIELDS_EXPLAINED.md    # AgentState详解
└── ANTHROPIC_AGENT_README.md      # Anthropic Agent完整指南

```

## 🚀 快速开始

### 1. 安装依赖

```bash
# 基础依赖
pip install langchain langchain-anthropic python-dotenv

# 可选：LangGraph支持
pip install langgraph

# 可选：OpenAI支持
pip install langchain-openai
```

### 2. 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的 API Keys
# ANTHROPIC_API_KEY=sk-ant-your-key-here
```

详细配置说明：[环境配置指南](docs/guides/ENV_CONFIG_GUIDE.md)

### 3. 运行第一个示例

```bash
# ⭐ 推荐：最简单的问答示例
python examples/use-agent-anthropic-qa-only.py

# 或者：带工具的Agent
python examples/use-agent-anthropic-simple.py

# 测试配置是否正确
python examples/test-anthropic-agent.py
```

## 📚 学习路径

### 🎯 初学者（第1-2周）

#### Day 1-2: 基础入门
- 阅读 [ANTHROPIC_AGENT_README.md](ANTHROPIC_AGENT_README.md)
- 运行 `examples/use-agent-anthropic-qa-only.py`
- 理解基本的LLM调用和消息格式

#### Day 3-4: 工具使用
- 学习 `examples/use-agent-tool.py`
- 尝试 `examples/use-agent-anthropic-simple.py`
- 创建自己的简单工具

#### Day 5-7: API集成
- 阅读 [天气API指南](docs/guides/WEATHER_API_GUIDE.md)
- 运行 `examples/use-agent-tool-real-weather.py`
- 集成其他外部API

### 🚀 中级（第3-4周）

#### Day 8-10: 状态管理
- 阅读 [AgentState详解](docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md)
- 学习 `examples/use-agent-with-memory-1.py`
- 理解状态的持久化

#### Day 11-14: 生产级实现
- 阅读 [用户信息管理](docs/guides/HOW_TO_FILL_USER_INFO.md)
- 研究 `examples/use-agent-with-memory-realistic.py`（⭐ 重点）
- 实现完整的用户会话管理

### 🎓 高级（第5-6周）

#### Day 15-18: LangGraph深入
- 学习 `examples/use-agent-anthropic-langgraph.py`
- 阅读 [create_agent源码分析](docs/advanced/create-agent-analysis.md)
- 理解状态图的工作原理

#### Day 19-21: 结构化输出
- 阅读 [ToolStrategy原理](docs/advanced/tool-strategy-analysis.md)
- 实现自定义的结构化输出
- 使用Pydantic模型验证

#### Day 22-30: 综合项目
- 构建完整的智能客服系统
- 实现多轮对话和上下文管理
- 添加错误处理和日志记录

## 🎯 示例说明

### 基础示例

#### 1. 纯问答（⭐ 推荐入门）
**文件**: `examples/use-agent-anthropic-qa-only.py`

最简单的实现，直接使用ChatAnthropic模型：
```python
from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
response = model.invoke([HumanMessage(content="你好")])
```

**适合**: 纯对话场景，不需要工具调用

#### 2. 带工具的Agent（⭐ 推荐学习）
**文件**: `examples/use-agent-anthropic-simple.py`

使用Agent框架，支持工具调用：
```python
from langchain.agents import create_agent
agent = create_agent(model=model, tools=[calculator_tool])
```

**适合**: 需要调用外部工具或API的场景

#### 3. LangGraph版本
**文件**: `examples/use-agent-anthropic-langgraph.py`

使用LangGraph构建状态图：
```python
from langgraph.graph import StateGraph
workflow = StateGraph(MessagesState)
```

**适合**: 复杂的多步骤工作流

### 工具集成示例

#### 4. 基础工具
**文件**: `examples/use-agent-tool.py`

创建简单的工具：
```python
@tool
def calculator(expression: str) -> str:
    """执行数学计算"""
    return str(eval(expression))
```

#### 5. 真实API集成（⭐ 实用）
**文件**: `examples/use-agent-tool-real-weather.py`

集成OpenWeatherMap API：
- 真实的HTTP请求
- 错误处理
- 数据解析

参考指南：[天气API指南](docs/guides/WEATHER_API_GUIDE.md)

### 记忆管理示例

#### 6. 基础记忆
**文件**: `examples/use-agent-with-memory-1.py`

简单的对话历史记录

#### 7. 改进的记忆
**文件**: `examples/use-agent-with-memory-improved.py`

添加检查点和持久化

#### 8. 生产级实现（⭐⭐⭐ 重点学习）
**文件**: `examples/use-agent-with-memory-realistic.py`

完整的用户会话管理：
- 从数据库获取用户信息
- 自定义State Schema
- 会话持久化
- 包装函数自动填充

参考指南：[用户信息管理](docs/guides/HOW_TO_FILL_USER_INFO.md)

### 测试和工具

#### 9. 测试脚本
**文件**: `examples/test-anthropic-agent.py`

验证配置和基本功能

#### 10. 状态字段对比
**文件**: `examples/compare-state-fields.py`

比较不同State Schema的区别

## 📖 文档说明

### 使用指南（`docs/guides/`）

1. **[环境配置指南](docs/guides/ENV_CONFIG_GUIDE.md)**
   - API Keys配置
   - 支持的模型
   - 代理设置

2. **[天气API指南](docs/guides/WEATHER_API_GUIDE.md)**
   - 如何注册OpenWeatherMap
   - 集成步骤
   - 完整代码示例

3. **[用户信息管理](docs/guides/HOW_TO_FILL_USER_INFO.md)**（⭐ 重要）
   - 从认证系统获取用户信息
   - 自定义State Schema
   - 生产环境最佳实践

### 进阶文档（`docs/advanced/`）

1. **[create_agent源码分析](docs/advanced/create-agent-analysis.md)**
   - Agent创建的完整流程
   - 状态图的构建
   - Middleware机制

2. **[ToolStrategy原理](docs/advanced/tool-strategy-analysis.md)**
   - 结构化输出的实现
   - Tool vs Provider策略
   - 自定义Schema

3. **[AgentState详解](docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md)**
   - 核心字段说明
   - 自定义字段
   - 状态更新机制

## 🔧 技术栈

- **Python**: 3.9+
- **LangChain**: 最新版本
- **LangGraph**: 最新版本（可选）
- **LLM提供商**:
  - Anthropic Claude（主要）
  - OpenAI GPT（可选）

## 💡 最佳实践

### 1. 开发环境
- 使用虚拟环境（venv或conda）
- 保持依赖更新：`pip install --upgrade langchain langchain-anthropic`

### 2. API使用
- 开发时使用成本较低的模型（如`claude-3-haiku`）
- 生产环境使用性能较好的模型（如`claude-3-5-sonnet`）
- 设置合理的token限制

### 3. 错误处理
- 所有生产代码都应该有try-except
- 实现重试机制（网络错误）
- 记录日志便于调试

### 4. 安全性
- 永远不要提交`.env`文件到Git
- 定期更换API Keys
- 使用环境变量管理敏感信息

## 🐛 常见问题

### Q1: 导入错误怎么办？
```bash
# 确保安装了正确的包
pip install langchain-anthropic  # 注意是 langchain-anthropic 不是 langchain_anthropic
```

### Q2: API调用失败？
- 检查`.env`文件是否在正确位置
- 验证API Key格式（应以`sk-ant-`开头）
- 运行测试脚本：`python examples/test-anthropic-agent.py`

### Q3: 如何使用代理？
在`.env`中添加：
```bash
ANTHROPIC_BASE_URL=https://your-proxy-url.com/v1
```

### Q4: 需要安装哪些依赖？
```bash
# 最小依赖（Anthropic Agent）
pip install langchain langchain-anthropic python-dotenv

# 完整依赖（包含所有功能）
pip install langchain langchain-anthropic langchain-openai langgraph python-dotenv requests
```

## 📚 学习资源

### 官方文档
- [LangChain官方文档](https://python.langchain.com/)
- [LangGraph文档](https://langchain-ai.github.io/langgraph/)
- [Anthropic文档](https://docs.anthropic.com/)

### 社区
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [LangChain Discord](https://discord.gg/langchain)

## 🎓 推荐阅读顺序

1. ✅ **第一步**: [ANTHROPIC_AGENT_README.md](ANTHROPIC_AGENT_README.md)
2. ✅ **配置**: [环境配置指南](docs/guides/ENV_CONFIG_GUIDE.md)
3. ✅ **运行**: `examples/use-agent-anthropic-qa-only.py`
4. ✅ **工具**: `examples/use-agent-tool-real-weather.py`
5. ✅ **状态**: [用户信息管理](docs/guides/HOW_TO_FILL_USER_INFO.md)
6. ✅ **实践**: `examples/use-agent-with-memory-realistic.py`
7. ✅ **进阶**: [create_agent源码分析](docs/advanced/create-agent-analysis.md)

## 📝 更新日志

- **2026-03-04**: 重新整理项目结构，优化文档组织
- **2024-02-10**: 添加Anthropic Agent完整文档
- **2024-02-09**: 添加记忆管理和用户状态示例
- **2024-02-08**: 初始化项目，添加基础示例

## 📧 获取帮助

如有问题：
1. 先查看 [常见问题](#-常见问题)
2. 运行测试脚本验证配置
3. 查阅相关文档
4. 提交Issue或联系维护者

---

**开始学习**: 从阅读 [ANTHROPIC_AGENT_README.md](ANTHROPIC_AGENT_README.md) 开始你的学习之旅！🚀
