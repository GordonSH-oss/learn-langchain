# learn-langchain 文件结构

```
learn-langchain/
├── README.md                              # 📘 项目总览和快速开始
├── ANTHROPIC_AGENT_README.md              # 📗 Anthropic Agent完整指南
├── .env.example                           # ⚙️  环境变量模板
│
├── examples/                              # 💻 示例代码
│   ├── use-agent-anthropic-qa-only.py             ⭐ 最简单：纯问答
│   ├── use-agent-anthropic-simple.py              ⭐ 推荐：带工具的Agent
│   ├── use-agent-anthropic-langgraph.py           LangGraph版本
│   ├── use-agent-tool.py                          基础工具示例
│   ├── use-agent-tool-real-weather.py             真实API集成
│   ├── use-agent-with-memory-1.py                 记忆系统v1
│   ├── use-agent-with-memory-improved.py          记忆系统v2
│   ├── use-agent-with-memory-realistic.py         ⭐ 生产级记忆
│   ├── test-anthropic-agent.py                    测试脚本
│   └── compare-state-fields.py                    状态字段对比
│
├── docs/                                  # 📚 文档
│   ├── guides/                            # 使用指南
│   │   ├── ENV_CONFIG_GUIDE.md                    环境配置指南
│   │   ├── WEATHER_API_GUIDE.md                   天气API集成
│   │   └── HOW_TO_FILL_USER_INFO.md               ⭐ 用户信息管理
│   │
│   └── advanced/                          # 进阶文档
│       ├── create-agent-analysis.md               create_agent源码分析
│       ├── tool-strategy-analysis.md              ToolStrategy原理
│       └── AGENT_STATE_FIELDS_EXPLAINED.md        AgentState详解
│
└── .archive/                              # 🗄️ 归档文件
    ├── ANTHROPIC_FIX_NOTES.md
    └── QUICKSTART_ANTHROPIC.md
```

## 文件说明

### 📘 核心文档
- **README.md**: 项目总览、快速开始、学习路径
- **ANTHROPIC_AGENT_README.md**: Anthropic Agent的完整使用指南

### 💻 示例代码（examples/）
所有示例都可以直接运行，按推荐度标记了⭐

**入门级**:
- `use-agent-anthropic-qa-only.py` - 最简单的实现
- `use-agent-anthropic-simple.py` - 带工具支持

**进阶**:
- `use-agent-tool-real-weather.py` - API集成示例
- `use-agent-with-memory-realistic.py` - 生产级状态管理

**测试**:
- `test-anthropic-agent.py` - 验证配置
- `compare-state-fields.py` - 学习State结构

### 📚 文档（docs/）

**guides/** - 实用指南:
- 环境配置
- API集成教程
- 生产环境最佳实践

**advanced/** - 深度解析:
- 源码分析
- 工作原理
- 核心概念详解

### 🗄️ 归档（.archive/）
已整合到其他文档的旧版本文件

## 快速导航

### 我是新手，从哪里开始？
1. 阅读 `README.md`
2. 配置环境（参考 `docs/guides/ENV_CONFIG_GUIDE.md`）
3. 运行 `examples/use-agent-anthropic-qa-only.py`

### 我想学习完整的Agent
1. 阅读 `ANTHROPIC_AGENT_README.md`
2. 运行 `examples/use-agent-anthropic-simple.py`
3. 学习 `docs/advanced/create-agent-analysis.md`

### 我要做生产项目
1. 学习 `docs/guides/HOW_TO_FILL_USER_INFO.md` ⭐
2. 研究 `examples/use-agent-with-memory-realistic.py` ⭐
3. 参考所有 `docs/advanced/` 的文档

### 我想集成API
1. 阅读 `docs/guides/WEATHER_API_GUIDE.md`
2. 运行 `examples/use-agent-tool-real-weather.py`
3. 根据需求修改代码
