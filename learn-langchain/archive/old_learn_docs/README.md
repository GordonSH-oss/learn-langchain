# LangChain & LangGraph 精通教程

> 从零基础到精通 LangChain、LangGraph 和 DeepAgents 的完整学习路径（60天）

## 📚 项目结构

```
learn-langchain-langgraph/
├── README.md                    # 本文件 - 总览和目录
│
├── 📅 学习计划（核心文档）
│   ├── CURRICULUM_MASTER.md            ⭐ 60天精通计划（推荐）
│   ├── CURRICULUM_WEEK2-8.md           📖 Week 2-8 详细内容
│   ├── DEEPAGENTS_GUIDE.md             🚀 DeepAgents 完全指南
│   ├── CURRICULUM.md                   📝 原30天计划（已备份）
│   └── CURRICULUM_30days_backup.md     💾 30天计划备份
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
├── langchain/                   # LangChain 源码（供参考学习）
└── deepagents/                  # DeepAgents 源码（供参考学习）
```

## 🎯 学习目标

完成本教程后，你将能够：

### 1. 🔰 LangChain 核心掌握
   - ✅ 深入理解 LLM、Prompt、Chain、Memory 等核心概念
   - ✅ 熟练使用各种 LLM 提供商（OpenAI、Anthropic 等）
   - ✅ 掌握 RAG（检索增强生成）技术
   - ✅ 实现复杂的 Chain 组合和 LCEL

### 2. 🔄 LangGraph 精通
   - ✅ 理解状态图（StateGraph）原理
   - ✅ 掌握节点、边、条件路由
   - ✅ 实现检查点和持久化
   - ✅ 构建复杂的工作流和状态机

### 3. 🚀 DeepAgents 应用
   - ✅ 使用 DeepAgents 构建多 Agent 系统
   - ✅ 实现 Agent 间协作和任务分配
   - ✅ 掌握层级管理模式
   - ✅ 应用高级 Agent 模式

### 4. 🏭 生产级开发
   - ✅ 性能优化和成本控制
   - ✅ 错误处理和容错机制
   - ✅ 监控、日志和调试
   - ✅ 部署和维护生产应用

## 📅 60天精通计划概览

### 🔰 第一阶段：LangChain 基础（Week 1-2，Day 1-14）
**核心内容**：
- Week 1: LLM调用、消息系统、Prompt工程、Chain和LCEL、输出解析器、检索基础
- Week 2: Tools工具系统、真实API集成、Agent创建、记忆管理、结构化输出

**项目**：智能文档助手、智能客服系统

### 🤖 第二阶段：Agent 和工具（Week 3-4，Day 15-28）
**核心内容**：
- Week 3: LangGraph StateGraph、节点和边、检查点和持久化
- Week 4: 高级Agent模式、Multi-Agent协作、中间件和扩展

**项目**：工作流自动化系统（代码审查/数据分析/内容生成）

### 🚀 第三阶段：DeepAgents（Week 5-6，Day 29-42）
**核心内容**：
- Week 5: DeepAgents架构、核心功能、工具系统、多Agent协作
- Week 6: 企业级功能、高级模式（Planning/Reflection/Self-improvement）

**项目**：智能代码助手（代码分析、Bug检测、重构建议、测试生成）

### 🏭 第四阶段：生产实践（Week 7-8，Day 43-60）
**核心内容**：
- Week 7: 性能优化、监控和调试、错误处理
- Week 8: 部署策略、安全合规、成本优化

**毕业项目**：完整的生产级AI应用

## 🚀 快速开始（5分钟）

### 1. 安装依赖

```bash
# 创建虚拟环境（推荐使用 virtualenvwrapper）
mkvirtualenv -p python3.12 langchain-master

# 或使用 venv
python3.12 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows

# 进入项目目录
cd learn-langchain

# 安装基础依赖
pip install langchain langchain-anthropic langchain-openai python-dotenv

# 安装 LangGraph（必需）
pip install langgraph

# 安装 DeepAgents（Week 5-6 会用到）
pip install deepagents
```

### 2. 配置 API Key

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env，填入你的 API Keys
# ANTHROPIC_API_KEY=sk-ant-your-key-here
# OPENAI_API_KEY=sk-your-key-here  # 可选，用于 embeddings
```

**获取 API Key**：
- Anthropic: [Anthropic Console](https://console.anthropic.com/)
- OpenAI: [OpenAI Platform](https://platform.openai.com/)

详细配置指南：[ENV_CONFIG_GUIDE.md](./learn-langchain/docs/guides/ENV_CONFIG_GUIDE.md)

### 3. 运行第一个示例

```bash
# 最简单的问答示例（推荐新手）
python examples/use-agent-anthropic-qa-only.py

# 或者测试配置是否正确
python examples/test-anthropic-agent.py
```

## 📖 文档导航

### ⚡ 快速入口
- **[QUICK_START.md](./QUICK_START.md)** 🚀🚀🚀
  - **5分钟快速导航**，帮你选择学习路径
  - 不知道从哪开始？先看这个！
  - 包含学习检查清单和常见问题

### 🆕 最新更新（2026年3月）
- **[CURRICULUM_UPDATES_2026.md](./CURRICULUM_UPDATES_2026.md)** ⭐⭐⭐ NEW!
  - **LangChain v1.0 和 LangGraph v1.0 最新特性**
  - create_agent 新API使用指南
  - 重要的迁移和更新说明
  - 基于最新官方文档（通过 MCP 获取）

### 🌟 核心学习计划（必读）
1. **[CURRICULUM_MASTER.md](./CURRICULUM_MASTER.md)** ⭐⭐⭐
   - 60天精通计划总览
   - Week 1 详细内容（Day 1-7）
   - 每日学习目标、实践任务、作业

2. **[CURRICULUM_WEEK2-8.md](./CURRICULUM_WEEK2-8.md)** ⭐⭐⭐
   - Week 2-8 详细内容
   - Agent、LangGraph、DeepAgents、生产实践
   - 项目和评估标准

3. **[DEEPAGENTS_GUIDE.md](./DEEPAGENTS_GUIDE.md)** ⭐⭐⭐
   - DeepAgents 完全指南
   - 核心概念、快速开始、深入教程
   - 实战项目、最佳实践

### 🎯 实战项目
- **[PROJECT_DOCUSAURUS_QA.md](./PROJECT_DOCUSAURUS_QA.md)** 🔥🔥🔥 NEW!
  - **Docusaurus 文档智能问答助手**
  - 学习如何构建文档问答系统
  - 包含完整代码和分步教程
  - 涵盖文档加载、向量检索、问答Agent
  - 适合 Week 2 完成后实践

### 📘 原有文档（仍然有效）
- **[CURRICULUM.md](./CURRICULUM.md)** - 原30天学习计划
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

- **Python**: 3.11+ （推荐 3.12）
- **核心框架**:
  - LangChain: 最新版本
  - LangGraph: 最新版本
  - DeepAgents: 最新版本
- **LLM 提供商**:
  - Anthropic Claude (推荐，主要使用)
  - OpenAI GPT (用于 embeddings 和对比)
  - 其他兼容 OpenAI API 的服务
- **开发工具**:
  - virtualenvwrapper 或 venv（虚拟环境）
  - python-dotenv（环境变量管理）
  - LangSmith（可选，用于监控和调试）

## 📚 学习路径

### 🎯 新手入门（第1周，推荐路径）

1. **Day 1**: 阅读本 README 和 [CURRICULUM_MASTER.md](./CURRICULUM_MASTER.md)
2. **Day 2**: 配置环境并运行第一个示例
3. **Day 3-4**: 学习消息系统和 Prompt 工程
4. **Day 5-7**: Chain、输出解析器、RAG 基础

### 🚀 系统学习（60天计划）

完整的 60 天学习计划请查看：**[CURRICULUM_MASTER.md](./CURRICULUM_MASTER.md)** （⭐⭐⭐ 强烈推荐）

学习计划包括：
- 📅 **每天的学习目标**：明确的学习重点
- 💻 **配套实践任务**：边学边练的代码示例
- 🎯 **周末综合项目**：巩固所学知识
- 📝 **学习评估**：检查学习效果
- 🚀 **进阶方向**：持续提升的路径

### 📖 按主题学习

#### 主题1：LangChain 基础（Week 1-2）
- [CURRICULUM_MASTER.md](./CURRICULUM_MASTER.md) - Week 1 详细内容
- [CURRICULUM_WEEK2-8.md](./CURRICULUM_WEEK2-8.md) - Week 2 详细内容
- [learn-langchain/README.md](./learn-langchain/README.md) - 配套示例

#### 主题2：LangGraph（Week 3-4）
- [CURRICULUM_WEEK2-8.md](./CURRICULUM_WEEK2-8.md) - Week 3-4 内容
- [learn-langchain/docs/advanced/](./learn-langchain/docs/advanced/) - 进阶文档

#### 主题3：DeepAgents（Week 5-6）
- [DEEPAGENTS_GUIDE.md](./DEEPAGENTS_GUIDE.md) - 完全指南 ⭐⭐⭐
- 包含概念、教程、项目、最佳实践

#### 主题4：生产实践（Week 7-8）
- [CURRICULUM_WEEK2-8.md](./CURRICULUM_WEEK2-8.md) - Week 7-8 内容
- [learn-langchain/docs/guides/HOW_TO_FILL_USER_INFO.md](./learn-langchain/docs/guides/HOW_TO_FILL_USER_INFO.md) - 生产最佳实践

### 🎓 进阶学习（完成60天后）

1. **深入源码**：
   - 研究 [create_agent源码分析](./learn-langchain/docs/advanced/create-agent-analysis.md)
   - 学习 [ToolStrategy原理](./learn-langchain/docs/advanced/tool-strategy-analysis.md)

2. **实战项目**：
   - 构建自己的完整项目
   - 参考 [DeepAgents 实战项目](./DEEPAGENTS_GUIDE.md#-实战项目)

3. **持续精进**：
   - 阅读最新论文和技术文章
   - 参与开源贡献
   - 关注社区最佳实践

## 📚 官方资源

### 核心文档
- [LangChain 官方文档](https://python.langchain.com/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [DeepAgents GitHub](https://github.com/deepagents/deepagents)
- [Anthropic 文档](https://docs.anthropic.com/)
- [OpenAI 文档](https://platform.openai.com/docs)

### 🆕 通过 MCP 访问最新文档
本课程使用 **Docs by LangChain MCP** 服务获取最新信息：
- ✅ 实时访问 LangChain 官方文档
- ✅ 确保课程内容始终最新
- ✅ 基于 LangChain v1.0 和 LangGraph v1.0

**什么是 MCP？**
Model Context Protocol（模型上下文协议）- 由 Anthropic 开发的标准协议，允许 AI 助手实时访问外部数据源。

### GitHub 仓库
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [DeepAgents GitHub](https://github.com/deepagents/deepagents)

### 社区资源
- [LangChain Discord](https://discord.gg/langchain)
- [LangChain Twitter](https://twitter.com/langchainai)
- [DeepLearning.AI LangChain Courses](https://www.deeplearning.ai/)
- [LangChain 中文社区](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)

## 📝 更新日志

### 2026-03-04 - 重大更新 v2.0 🎉
- ✅ **新增**：基于 MCP 的最新内容更新（`CURRICULUM_UPDATES_2026.md`）
  - LangChain v1.0 新特性和迁移指南
  - LangGraph v1.0 稳定版更新
  - create_agent 新API详解
  - 中间件（Middleware）使用指南
- ✅ **新增**：Docusaurus 文档问答助手实战项目（`PROJECT_DOCUSAURUS_QA.md`）
  - 完整的文档加载和处理流程
  - 向量检索和RAG实现
  - CLI和Web界面实现
  - 生产级优化建议
- ✅ **更新**：所有教程内容基于最新官方文档验证

### 2026-03-04 - 重大更新 v1.0 🎉
- ✅ 创建 60 天精通计划（`CURRICULUM_MASTER.md`）
- ✅ 添加 Week 2-8 详细内容（`CURRICULUM_WEEK2-8.md`）
- ✅ 新增 DeepAgents 完全指南（`DEEPAGENTS_GUIDE.md`）
- ✅ 重新组织文档结构，添加更多实战项目
- ✅ 扩充内容：从 30 天基础课程升级为 60 天精通路径
- ✅ 新增主题：DeepAgents、生产实践、性能优化、部署维护

### 2026-03-04 - 文件整理
- ✅ 重新整理项目结构
- ✅ 优化文档组织
- ✅ 创建 30 天学习计划（现已升级为 60 天）

### 2024-02 - 初始版本
- 添加 Anthropic Agent 完整文档
- 添加记忆管理和状态示例
- 初始化项目

## ⚠️ 重要提示

### 安全和隐私
- 🔒 **永远不要将 `.env` 文件提交到 Git**
- 🔑 定期更换 API Keys
- 🚫 不要在代码中硬编码敏感信息
- 📝 使用 `.gitignore` 忽略敏感文件

### 成本控制
- 💰 注意 API 调用次数和费用
- 📊 监控 API 使用情况（使用各平台的 Dashboard）
- ⚡ 合理使用缓存减少重复调用
- 🎯 选择合适的模型（不是越贵越好）

### 学习建议
- 📚 **循序渐进**：按照课程计划学习，不要跳跃
- 💻 **动手实践**：每天都要写代码，不能只看不练
- 📝 **记录笔记**：整理学习心得和问题
- 🤝 **积极交流**：加入社区，提问和讨论
- 🎯 **项目驱动**：结合实际项目学习效果最好

---

## 🚀 开始学习

### 推荐学习路径

**第1步：快速体验（Day 1）**
1. ✅ 阅读本 README，了解整体结构
2. ✅ 按照 [快速开始](#-快速开始) 配置环境
3. ✅ 运行第一个示例 `examples/use-agent-anthropic-qa-only.py`
4. ✅ 感受一下 LangChain 的魅力

**第2步：系统学习（Day 2-60）**
1. ✅ 打开 [CURRICULUM_MASTER.md](./CURRICULUM_MASTER.md) 查看详细计划
2. ✅ 每天按计划学习 2-3 小时
3. ✅ 完成每日的实践任务和作业
4. ✅ 周末完成综合项目

**第3步：深入实践（Week 5-6）**
1. ✅ 学习 [DEEPAGENTS_GUIDE.md](./DEEPAGENTS_GUIDE.md)
2. ✅ 构建多 Agent 协作系统
3. ✅ 完成实战项目

**第4步：生产应用（Week 7-8）**
1. ✅ 学习性能优化和部署
2. ✅ 完成毕业项目
3. ✅ 发布你的第一个 AI 应用

### 学习检查点

每周结束时，检查自己是否达到以下目标：

**Week 1-2 检查点**：
- [ ] 能独立创建 LangChain 应用
- [ ] 理解 Prompt、Chain、Memory 概念
- [ ] 会创建和使用工具
- [ ] 完成周末项目

**Week 3-4 检查点**：
- [ ] 熟练使用 LangGraph
- [ ] 能构建复杂状态机
- [ ] 理解检查点和持久化
- [ ] 完成工作流项目

**Week 5-6 检查点**：
- [ ] 掌握 DeepAgents 框架
- [ ] 能构建多 Agent 系统
- [ ] 完成代码助手项目

**Week 7-8 检查点**：
- [ ] 能优化和调试应用
- [ ] 能部署生产应用
- [ ] 完成毕业项目

---

## 💬 获取帮助

遇到问题？试试这些方法：

1. **查看文档**：先查阅相关文档，90%的问题都有答案
2. **示例代码**：参考 `examples/` 目录下的示例
3. **搜索 Issues**：GitHub Issues 里可能有类似问题
4. **社区提问**：
   - LangChain Discord
   - GitHub Discussions
   - Stack Overflow（标签：langchain）
5. **官方文档**：查阅 LangChain/LangGraph 官方文档

---

**记住：实践是最好的老师！** 

多写代码、多实验、多思考。坚持 60 天，你将从零基础成为 LangChain 专家！

祝学习愉快！🎉 加油！💪
