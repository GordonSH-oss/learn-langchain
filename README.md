# LangChain & LangGraph 学习教程

> 系统化学习 LangChain 和 LangGraph 开发的完整教程

## 📚 项目结构

```
learn-langchain-langgraph/
├── README.md                    # 本文件 - 总览和目录
├── CURRICULUM.md                # 📅 30天详细学习计划
│
├── learn-langchain/             # 💻 实践代码和文档
│   ├── README.md                       # 项目说明和快速开始
│   ├── FILE_STRUCTURE.md               # 详细的文件结构说明
│   ├── ANTHROPIC_AGENT_README.md       # Anthropic Agent完整指南
│   │
│   ├── examples/                       # 示例代码（10个示例）
│   │   ├── use-agent-anthropic-*.py           基础Agent示例
│   │   ├── use-agent-tool-*.py                工具使用示例
│   │   └── use-agent-with-memory-*.py         记忆管理示例
│   │
│   └── docs/                           # 学习文档
│       ├── guides/                            使用指南（3篇）
│       └── advanced/                          进阶文档（3篇）
│
└── langchain/                   # LangChain 源码（供参考学习）
```

## 🎯 学习目标

通过本教程，你将：

1. **掌握 LangChain 基础**
   - 理解 LLM、Prompt、Chain 等核心概念
   - 学会使用各种 LLM 提供商（OpenAI、Anthropic 等）
   - 掌握记忆管理和对话上下文

2. **精通 LangGraph 开发**
   - 理解状态图（StateGraph）原理
   - 掌握 Agent 的创建和配置
   - 学会使用工具（Tools）和中间件（Middleware）

3. **构建生产级应用**
   - 实现持久化和检查点（Checkpoint）
   - 处理错误和异常
   - 性能优化和最佳实践

## 📅 学习计划概览

### 第一周：LangChain 基础入门
- **Day 1-2**: 环境搭建、基本概念、第一个 LLM 应用
- **Day 3-4**: Prompt 工程、对话管理
- **Day 5-7**: Chain 组合、输出解析器、记忆系统

### 第二周：工具和 Agent 基础
- **Day 8-9**: 工具（Tools）的创建和使用
- **Day 10-11**: Agent 基础概念和简单 Agent
- **Day 12-14**: Agent 实践：计算器、天气查询、搜索

### 第三周：LangGraph 核心
- **Day 15-16**: StateGraph 原理和基础使用
- **Day 17-18**: 条件边和路由
- **Day 19-21**: 高级 Agent、结构化输出、中间件

### 第四周：生产实践和项目
- **Day 22-23**: 持久化、检查点、状态管理
- **Day 24-25**: 错误处理、重试策略、性能优化
- **Day 26-28**: 综合项目：智能客服系统
- **Day 29-30**: 总结、最佳实践、进阶方向

## 🚀 快速开始（5分钟）

### 1. 安装依赖

```bash
# 进入项目目录
cd learn-langchain

# 安装基础依赖
pip install langchain langchain-anthropic python-dotenv

# 可选：安装 LangGraph 支持
pip install langgraph
```

### 2. 配置 API Key

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env，填入你的 Anthropic API Key
# ANTHROPIC_API_KEY=sk-ant-your-key-here
```

获取 API Key: [Anthropic Console](https://console.anthropic.com/)

详细配置指南：[ENV_CONFIG_GUIDE.md](./learn-langchain/docs/guides/ENV_CONFIG_GUIDE.md)

### 3. 运行第一个示例

```bash
# 最简单的问答示例（推荐新手）
python examples/use-agent-anthropic-qa-only.py

# 或者测试配置是否正确
python examples/test-anthropic-agent.py
```

## 📖 文档导航

### 📘 核心文档
- **[CURRICULUM.md](./CURRICULUM.md)** - 30天详细学习计划（⭐ 推荐）
- **[learn-langchain/README.md](./learn-langchain/README.md)** - 项目说明和快速开始
- **[learn-langchain/ANTHROPIC_AGENT_README.md](./learn-langchain/ANTHROPIC_AGENT_README.md)** - Anthropic Agent完整指南

### 📚 使用指南（learn-langchain/docs/guides/）
- [环境配置指南](./learn-langchain/docs/guides/ENV_CONFIG_GUIDE.md) - API Keys和模型配置
- [天气API指南](./learn-langchain/docs/guides/WEATHER_API_GUIDE.md) - 外部API集成示例
- [用户信息管理](./learn-langchain/docs/guides/HOW_TO_FILL_USER_INFO.md) - 生产环境最佳实践（⭐ 重要）

### 🎓 进阶文档（learn-langchain/docs/advanced/）
- [create_agent源码分析](./learn-langchain/docs/advanced/create-agent-analysis.md) - Agent创建流程深度解析
- [ToolStrategy原理](./learn-langchain/docs/advanced/tool-strategy-analysis.md) - 结构化输出实现细节
- [AgentState详解](./learn-langchain/docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md) - 状态管理核心概念

## 💻 示例代码（learn-langchain/examples/）

所有示例代码都已整理到 `learn-langchain/examples/` 目录下，可以直接运行。

### 入门示例
- ⭐ **use-agent-anthropic-qa-only.py** - 最简单的问答（推荐新手）
- ⭐ **use-agent-anthropic-simple.py** - 带工具的Agent（推荐学习）
- **use-agent-anthropic-langgraph.py** - LangGraph版本

### 工具集成
- **use-agent-tool.py** - 基础工具创建
- **use-agent-tool-real-weather.py** - 真实API集成示例

### 记忆管理
- **use-agent-with-memory-1.py** - 基础记忆
- **use-agent-with-memory-improved.py** - 改进版本
- ⭐ **use-agent-with-memory-realistic.py** - 生产级实现（重点学习）

### 测试工具
- **test-anthropic-agent.py** - 配置验证和测试
- **compare-state-fields.py** - State结构对比

详细说明请查看：[learn-langchain/FILE_STRUCTURE.md](./learn-langchain/FILE_STRUCTURE.md)

## 🔧 技术栈

- **Python**: 3.9+
- **LangChain**: 最新版本
- **LangGraph**: 最新版本
- **LLM 提供商**:
  - Anthropic Claude (推荐)
  - OpenAI GPT
  - 其他兼容 OpenAI API 的服务

## 📚 学习路径

### 🎯 新手入门（推荐路径）

1. **Day 1**: 阅读 [learn-langchain/README.md](./learn-langchain/README.md) 了解项目结构
2. **Day 2**: 配置环境并运行 `examples/use-agent-anthropic-qa-only.py`
3. **Day 3-5**: 学习 [ANTHROPIC_AGENT_README.md](./learn-langchain/ANTHROPIC_AGENT_README.md)
4. **Day 6-7**: 尝试其他示例代码，修改和实验

### 🚀 系统学习（30天计划）

详细的30天学习计划请查看：**[CURRICULUM.md](./CURRICULUM.md)** （⭐ 强烈推荐）

学习计划包括：
- 📅 每天的学习目标和内容
- 💻 配套的实践任务
- 🎯 周末的综合项目
- 📝 学习评估和检查点

### 🎓 进阶学习

1. 研究 [create_agent源码分析](./learn-langchain/docs/advanced/create-agent-analysis.md)
2. 学习 [ToolStrategy原理](./learn-langchain/docs/advanced/tool-strategy-analysis.md)
3. 实践 [用户信息管理](./learn-langchain/docs/guides/HOW_TO_FILL_USER_INFO.md)
4. 构建自己的完整项目

## 📚 官方资源

- [LangChain 官方文档](https://python.langchain.com/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [Anthropic 文档](https://docs.anthropic.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)

## ⚠️ 重要提示

- 🔒 永远不要将 `.env` 文件提交到 Git
- 💰 注意 API 调用次数和费用
- 🔄 定期更换 API Keys
- 📊 监控 API 使用情况

## 📝 更新日志

- **2026-03-04**: 🎉 重新整理项目结构，优化文档组织，创建30天学习计划
- **2024-02-10**: 添加 Anthropic Agent 完整文档
- **2024-02-09**: 添加记忆管理和状态示例
- **2024-02-08**: 初始化项目

---

## 🚀 开始学习

1. ✅ 阅读 [CURRICULUM.md](./CURRICULUM.md) - 查看30天学习计划
2. ✅ 按照 [快速开始](#-快速开始) 配置环境
3. ✅ 运行第一个示例 `examples/use-agent-anthropic-qa-only.py`
4. ✅ 坚持每天学习和实践

**记住：实践是最好的老师！** 多写代码、多实验、多思考。祝学习愉快！🎉
