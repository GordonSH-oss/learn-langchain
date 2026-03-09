# LangChain 实战精通课程 V3.0

> 🎯 **从零基础到源码掌握** - 8周系统学习 LangChain、LangGraph 和 DeepAgents

## 📋 课程特色

- ✅ **理论+实战**：每个知识点都有配套代码
- ✅ **循序渐进**：从简单到复杂，逐步深入
- ✅ **源码解读**：深入理解框架原理
- ✅ **项目驱动**：每周一个完整实战项目
- ✅ **生产就绪**：学习工业级开发技巧

## 🎓 学习路径

```
Week 1: LangChain 基础
  ├── Day 1: 环境搭建 & 第一个应用
  ├── Day 2: LLM调用与消息系统
  ├── Day 3: Prompt工程与模板
  ├── Day 4: Chain与LCEL
  ├── Day 5: 输出解析器
  ├── Day 6: 文档加载与RAG基础
  └── Day 7: 【项目】智能文档问答助手

Week 2: Agent与工具
  ├── Day 8: Tools工具系统
  ├── Day 9: Agent原理与create_agent
  ├── Day 10: 真实API集成（天气、搜索等）
  ├── Day 11: Memory记忆管理
  ├── Day 12: 结构化输出
  ├── Day 13: Agent进阶技巧
  └── Day 14: 【项目】智能客服系统

Week 3-4: LangGraph
  ├── Day 15-16: StateGraph基础
  ├── Day 17-18: 节点、边与路由
  ├── Day 19-20: 检查点与持久化
  ├── Day 21: 【项目】工作流自动化（代码审查）
  ├── Day 22-24: Multi-Agent协作
  ├── Day 25-27: 中间件与扩展
  └── Day 28: 【项目】多Agent内容生成系统

Week 5-6: DeepAgents
  ├── Day 29-30: DeepAgents架构与核心概念
  ├── Day 31-32: Agent、Task、Crew
  ├── Day 33-34: 工具系统与流程管理
  ├── Day 35: 【项目】智能代码助手 v1
  ├── Day 36-38: 高级模式（Planning/Reflection）
  ├── Day 39-41: 企业级功能
  └── Day 42: 【项目】智能代码助手 v2（完整版）

Week 7-8: 生产实践与源码
  ├── Day 43-45: 性能优化与成本控制
  ├── Day 46-47: 监控、日志与调试
  ├── Day 48-49: 源码解读 - LangChain核心
  ├── Day 50-51: 源码解读 - LangGraph实现
  ├── Day 52-53: 源码解读 - DeepAgents架构
  ├── Day 54-55: 部署与运维
  └── Day 56-60: 【毕业项目】完整的生产级AI应用
```

## 📚 Week 1: LangChain 基础

### 学习目标
- 搭建开发环境，运行第一个LangChain应用
- 理解LLM调用、消息系统、Prompt工程
- 掌握Chain组合和LCEL语法
- 学会使用输出解析器
- 了解文档加载和RAG基础
- **项目**：构建智能文档问答助手

### Day 1: 环境搭建 & 第一个应用

**📖 理论**
- LangChain生态系统概览
- 核心组件：LLM、Prompt、Chain、Agent、Memory
- LangChain vs 直接调用API的优势

**💻 实践**
```bash
# 1. 创建虚拟环境
mkvirtualenv -p python3.12 langchain-learn

# 2. 安装依赖
pip install langchain langchain-anthropic python-dotenv

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env，填入 ANTHROPIC_API_KEY

# 4. 运行第一个示例
python week1/day1_hello_langchain.py
```

**📝 示例代码**：`week1/day1_hello_langchain.py`
- 基础LLM调用
- 理解消息格式
- 简单的问答系统

**🎯 作业**
1. 成功运行示例代码
2. 修改system_prompt，创建不同性格的AI助手
3. 实现一个简单的翻译助手

---

### Day 2: LLM调用与消息系统

**📖 理论**
- Message类型：SystemMessage、HumanMessage、AIMessage
- 对话历史管理
- 温度参数与采样策略
- Token管理

**💻 实践**：`week1/day2_messages.py`
- 不同消息类型的使用
- 多轮对话实现
- 上下文管理

**🎯 作业**
1. 实现一个记录对话历史的聊天机器人
2. 测试不同temperature值对输出的影响
3. 实现token计数和限制

---

### Day 3: Prompt工程与模板

**📖 理论**
- Prompt工程最佳实践
- PromptTemplate使用
- Few-shot学习
- ChatPromptTemplate

**💻 实践**：`week1/day3_prompts.py`
- 创建可复用的Prompt模板
- Few-shot示例
- 动态变量插入

**🎯 作业**
1. 创建一个代码生成的Prompt模板
2. 实现Few-shot分类器
3. 设计一个SQL生成助手的Prompt

---

### Day 4: Chain与LCEL

**📖 理论**
- Chain的概念和类型
- LCEL (LangChain Expression Language)
- 链式调用与组合
- 管道操作符 `|`

**💻 实践**：`week1/day4_chains.py`
- 简单Chain
- SequentialChain
- LCEL语法
- 链的组合与嵌套

**🎯 作业**
1. 创建一个"分析-总结-评分"的Chain
2. 用LCEL实现复杂的数据处理流程
3. 实现一个文章改写Chain

---

### Day 5: 输出解析器

**📖 理论**
- StructuredOutputParser
- Pydantic OutputParser
- JSON输出解析
- 错误处理与重试

**💻 实践**：`week1/day5_output_parsers.py`
- 结构化输出
- Pydantic模型验证
- 输出格式化

**🎯 作业**
1. 创建一个返回结构化数据的Agent
2. 实现数据验证和错误处理
3. 设计一个产品信息提取器

---

### Day 6: 文档加载与RAG基础

**📖 理论**
- DocumentLoader概念
- 文本分割策略
- 向量数据库基础
- RAG (Retrieval Augmented Generation)

**💻 实践**：`week1/day6_rag_basics.py`
- 加载不同类型文档
- 文本分割
- 简单的检索系统

**🎯 作业**
1. 加载并处理自己的文档
2. 实现不同的分割策略对比
3. 构建基础的文档检索系统

---

### Day 7: 【项目】智能文档问答助手

**🎯 项目目标**
构建一个完整的文档问答系统，支持：
- 上传多种格式文档（txt, md, pdf）
- 智能分割和索引
- 基于上下文的问答
- CLI交互界面

**📁 项目结构**
```
week1_project_doc_qa/
├── README.md              # 项目说明
├── requirements.txt       # 依赖
├── .env.example          # 环境变量模板
├── main.py               # 主程序
├── doc_loader.py         # 文档加载模块
├── qa_chain.py           # 问答链模块
├── utils.py              # 工具函数
└── docs/                 # 示例文档
```

**✅ 评估标准**
- [ ] 成功加载和处理文档
- [ ] 准确回答基于文档的问题
- [ ] 引用来源信息
- [ ] 友好的用户界面
- [ ] 代码规范和注释

---

## 📚 Week 2: Agent与工具

### 学习目标
- 理解Agent的概念和工作原理
- 掌握Tools工具系统
- 学会集成真实的外部API
- 掌握记忆管理
- 理解结构化输出
- **项目**：构建智能客服系统

### Day 8: Tools工具系统

**📖 理论**
- Tool的定义和组成
- @tool装饰器
- StructuredTool
- Tool的参数定义（args_schema）

**💻 实践**：`week2/day8_tools.py`
- 创建简单工具
- 工具参数验证
- 工具组合

**🎯 作业**
1. 创建计算器工具
2. 实现文件读写工具
3. 创建时间转换工具

---

### Day 9: Agent原理与create_agent

**📖 理论**
- Agent的工作原理（ReAct模式）
- create_agent API详解
- Agent的配置选项
- 工具选择策略

**💻 实践**：`week2/day9_agent_basics.py`
- 创建第一个Agent
- Agent执行流程分析
- 配置不同参数

**🎯 作业**
1. 创建带多个工具的Agent
2. 分析Agent的决策过程
3. 实现自定义的工具选择逻辑

---

### Day 10: 真实API集成

**📖 理论**
- API认证和安全
- 错误处理和重试
- 速率限制
- API响应解析

**💻 实践**：`week2/day10_api_integration.py`
- 天气API集成
- 搜索API集成
- 新闻API集成

**🎯 作业**
1. 集成GitHub API（获取仓库信息）
2. 集成币种汇率API
3. 实现API调用的缓存机制

---

### Day 11: Memory记忆管理

**📖 理论**
- 记忆的类型（短期、长期）
- ConversationBufferMemory
- ConversationSummaryMemory
- 检查点（Checkpointer）

**💻 实践**：`week2/day11_memory.py`
- 实现对话记忆
- 使用不同的Memory类型
- 持久化对话历史

**🎯 作业**
1. 实现带记忆的聊天机器人
2. 对比不同Memory策略
3. 实现基于数据库的记忆存储

---

### Day 12: 结构化输出

**📖 理论**
- 结构化输出的必要性
- ToolStrategy vs ProviderStrategy
- 使用Pydantic定义Schema
- 输出验证

**💻 实践**：`week2/day12_structured_output.py`
- 定义复杂的输出Schema
- 结构化数据提取
- 输出格式化

**🎯 作业**
1. 创建简历信息提取器
2. 实现产品评论分析器
3. 设计会议纪要生成器

---

### Day 13: Agent进阶技巧

**📖 理论**
- Agent的调试方法
- 提高Agent准确性的技巧
- 工具描述的最佳实践
- 减少Token消耗

**💻 实践**：`week2/day13_agent_advanced.py`
- Agent调试技巧
- 优化工具描述
- 性能优化

**🎯 作业**
1. 优化一个现有Agent的性能
2. 实现Agent的日志记录
3. 对比不同配置的效果

---

### Day 14: 【项目】智能客服系统

**🎯 项目目标**
构建一个完整的智能客服系统，支持：
- 多意图识别
- 查询订单信息
- 产品推荐
- FAQ问答
- 人工转接

**📁 项目结构**
```
week2_project_customer_service/
├── README.md              # 项目说明
├── requirements.txt       # 依赖
├── .env.example          # 环境变量模板
├── main.py               # 主程序
├── agent/
│   ├── __init__.py
│   ├── customer_agent.py  # 客服Agent
│   └── tools.py          # 工具定义
├── database/
│   ├── __init__.py
│   ├── orders.py         # 订单数据
│   └── products.py       # 产品数据
├── memory/
│   ├── __init__.py
│   └── session.py        # 会话管理
└── tests/
    └── test_agent.py     # 测试用例
```

**✅ 评估标准**
- [ ] 准确识别用户意图
- [ ] 正确调用相应工具
- [ ] 记住对话上下文
- [ ] 友好的交互体验
- [ ] 完善的错误处理

---

## 📚 Week 3-4: LangGraph

### 学习目标
- 理解LangGraph的状态图模型
- 掌握节点、边、条件路由
- 学会使用检查点和持久化
- 实现Multi-Agent协作
- **项目**：工作流自动化系统

### Day 15-16: StateGraph基础

**📖 理论**
- 状态图的概念
- StateGraph vs Agent
- 节点(Node)和状态(State)
- 图的执行流程

**💻 实践**：`week3/day15_stategraph_basics.py`
- 创建第一个StateGraph
- 定义状态Schema
- 添加节点和边

**🎯 作业**
1. 创建一个简单的任务执行图
2. 实现条件分支
3. 可视化状态图

---

### Day 17-18: 节点、边与路由

**📖 理论**
- 条件边(conditional_edges)
- 动态路由
- 循环控制
- 并行执行

**💻 实践**：`week3/day17_routing.py`
- 实现条件路由
- 循环处理
- 并行节点

**🎯 作业**
1. 实现一个审批流程图
2. 创建循环重试逻辑
3. 设计并行处理任务

---

### Day 19-20: 检查点与持久化

**📖 理论**
- Checkpointer概念
- MemorySaver
- SqliteSaver
- 状态恢复

**💻 实践**：`week3/day19_checkpoints.py`
- 实现检查点
- 状态持久化
- 断点续传

**🎯 作业**
1. 实现基于SQLite的持久化
2. 创建可恢复的长任务
3. 实现状态版本管理

---

### Day 21: 【项目】工作流自动化（代码审查）

**🎯 项目目标**
构建一个自动化代码审查系统：
- 分析代码质量
- 检测潜在问题
- 生成改进建议
- 评分和报告

**📁 项目结构**
```
week3_project_code_review/
├── README.md
├── requirements.txt
├── main.py
├── graph/
│   ├── __init__.py
│   ├── review_graph.py    # 审查流程图
│   └── nodes.py          # 各个审查节点
├── analyzers/
│   ├── __init__.py
│   ├── style_checker.py  # 风格检查
│   ├── security_scan.py  # 安全扫描
│   └── performance.py    # 性能分析
└── reports/
    └── template.md       # 报告模板
```

**✅ 评估标准**
- [ ] 完整的审查流程
- [ ] 多维度分析
- [ ] 生成详细报告
- [ ] 可配置的规则
- [ ] 状态持久化

---

### Day 22-24: Multi-Agent协作

**📖 理论**
- Multi-Agent架构
- Agent间通信
- 任务分配策略
- 协作模式

**💻 实践**：`week4/day22_multi_agent.py`
- 创建多个Agent
- Agent间消息传递
- 协作完成任务

**🎯 作业**
1. 实现研究员-作家Agent协作
2. 创建任务分配系统
3. 设计Agent监督机制

---

### Day 25-27: 中间件与扩展

**📖 理论**
- Middleware概念
- 日志中间件
- 监控中间件
- 自定义扩展

**💻 实践**：`week4/day25_middleware.py`
- 实现日志中间件
- 性能监控
- 自定义中间件

**🎯 作业**
1. 实现Token使用统计中间件
2. 创建缓存中间件
3. 设计错误重试中间件

---

### Day 28: 【项目】多Agent内容生成系统

**🎯 项目目标**
构建一个多Agent协作的内容生成系统：
- 主题研究Agent
- 内容撰写Agent
- 编辑审核Agent
- SEO优化Agent

**📁 项目结构**
```
week4_project_content_system/
├── README.md
├── requirements.txt
├── main.py
├── agents/
│   ├── __init__.py
│   ├── researcher.py     # 研究Agent
│   ├── writer.py         # 写作Agent
│   ├── editor.py         # 编辑Agent
│   └── seo_optimizer.py  # SEO Agent
├── graph/
│   ├── __init__.py
│   └── workflow.py       # 工作流定义
└── outputs/
    └── articles/         # 生成的文章
```

**✅ 评估标准**
- [ ] 多Agent有效协作
- [ ] 生成高质量内容
- [ ] 完整的审核流程
- [ ] SEO优化建议
- [ ] 可追踪的工作流

---

## 📚 Week 5-6: DeepAgents

### 学习目标
- 理解DeepAgents框架
- 掌握Agent、Task、Crew概念
- 学会构建复杂的Multi-Agent系统
- 实现高级Agent模式
- **项目**：智能代码助手

### Day 29-30: DeepAgents架构与核心概念

**📖 理论**
- DeepAgents vs LangChain/LangGraph
- Agent角色定义
- Task任务系统
- Crew团队管理

**💻 实践**：`week5/day29_deepagents_intro.py`
- 创建第一个DeepAgents应用
- Agent角色配置
- Task定义

**🎯 作业**
1. 创建3个不同角色的Agent
2. 定义任务依赖关系
3. 实现简单的Crew

---

### Day 31-32: Agent、Task、Crew详解

**📖 理论**
- Agent属性详解（role, goal, backstory）
- Task配置（expected_output, context）
- Crew的Process类型（sequential, hierarchical, parallel）
- 回调和事件

**💻 实践**：`week5/day31_agent_task_crew.py`
- 复杂Agent配置
- Task链式依赖
- 不同Process模式

**🎯 作业**
1. 实现hierarchical流程
2. 创建带上下文的Task链
3. 配置回调函数

---

### Day 33-34: 工具系统与流程管理

**📖 理论**
- DeepAgents工具系统
- 自定义工具
- 工具权限管理
- 流程控制

**💻 实践**：`week5/day33_tools_process.py`
- 创建自定义工具
- 工具分配给Agent
- 流程编排

**🎯 作业**
1. 实现数据库查询工具
2. 创建API调用工具
3. 设计复杂的流程

---

### Day 35: 【项目】智能代码助手 v1

**🎯 项目目标**
构建一个基础的智能代码助手：
- 代码分析
- Bug检测
- 性能建议

**📁 项目结构**
```
week5_project_code_assistant_v1/
├── README.md
├── requirements.txt
├── main.py
├── agents/
│   ├── __init__.py
│   ├── analyzer.py       # 分析Agent
│   └── tester.py         # 测试Agent
└── tools/
    ├── __init__.py
    ├── ast_parser.py     # 代码解析
    └── linter.py         # 代码检查
```

**✅ 评估标准**
- [ ] 准确的代码分析
- [ ] 有用的建议
- [ ] 良好的报告格式

---

### Day 36-38: 高级模式（Planning/Reflection）

**📖 理论**
- Planning模式
- Reflection（自我反思）
- Self-improvement
- Meta-Agent

**💻 实践**：`week6/day36_advanced_patterns.py`
- 实现Planning Agent
- Reflection循环
- 自我优化

**🎯 作业**
1. 创建能规划的Agent
2. 实现自我纠错机制
3. 设计Meta-Agent

---

### Day 39-41: 企业级功能

**📖 理论**
- 错误处理和重试
- 监控和日志
- 成本控制
- 性能优化

**💻 实践**：`week6/day39_enterprise.py`
- 完善的错误处理
- 日志系统
- 性能监控

**🎯 作业**
1. 实现完整的错误处理
2. 添加性能监控
3. 优化Token使用

---

### Day 42: 【项目】智能代码助手 v2（完整版）

**🎯 项目目标**
升级为完整的智能代码助手：
- 代码分析（语法、风格、安全）
- Bug检测和修复建议
- 重构建议
- 测试生成
- 文档生成
- 性能优化建议

**📁 项目结构**
```
week6_project_code_assistant_v2/
├── README.md
├── requirements.txt
├── main.py
├── agents/
│   ├── __init__.py
│   ├── analyzer.py       # 分析Agent
│   ├── bug_hunter.py     # Bug检测Agent
│   ├── refactor.py       # 重构Agent
│   ├── tester.py         # 测试生成Agent
│   └── documenter.py     # 文档Agent
├── tools/
│   ├── __init__.py
│   ├── ast_parser.py     # AST解析
│   ├── linter.py         # Linter集成
│   ├── security_scan.py  # 安全扫描
│   └── profiler.py       # 性能分析
├── crew/
│   ├── __init__.py
│   └── code_review_crew.py  # Crew配置
└── reports/
    └── report_generator.py   # 报告生成
```

**✅ 评估标准**
- [ ] 全面的代码分析
- [ ] 准确的Bug检测
- [ ] 实用的重构建议
- [ ] 自动生成测试用例
- [ ] 完整的文档
- [ ] 性能优化建议
- [ ] 专业的报告

---

## 📚 Week 7-8: 生产实践与源码

### 学习目标
- 掌握性能优化技巧
- 学习监控和调试方法
- 深入理解框架源码
- 学会部署和运维
- **项目**：完整的生产级AI应用

### Day 43-45: 性能优化与成本控制

**📖 理论**
- Token优化策略
- 缓存机制
- 批处理
- 模型选择

**💻 实践**：`week7/day43_performance.py`
- 实现缓存
- 批量处理
- 性能监控

**🎯 作业**
1. 优化一个现有应用的性能
2. 实现智能缓存策略
3. 对比不同模型的成本

---

### Day 46-47: 监控、日志与调试

**📖 理论**
- LangSmith集成
- 日志最佳实践
- 调试技巧
- 追踪和分析

**💻 实践**：`week7/day46_monitoring.py`
- LangSmith设置
- 完善的日志系统
- 调试工具

**🎯 作业**
1. 集成LangSmith
2. 实现结构化日志
3. 创建调试面板

---

### Day 48-49: 源码解读 - LangChain核心

**📖 理论**
- LangChain架构设计
- 核心抽象类
- LCEL实现原理
- Runnable接口

**💻 实践**：`week7/day48_source_code_langchain.py`
- 阅读核心源码
- 理解设计模式
- 自定义组件

**📁 源码学习**
```
源码导读/langchain/
├── README.md                    # 源码学习指南
├── 01_architecture.md           # 架构概览
├── 02_runnable.md              # Runnable接口
├── 03_chains.md                # Chain实现
├── 04_agents.md                # Agent实现
└── annotated_code/             # 带注释的源码
    ├── base.py
    ├── chains/
    └── agents/
```

**🎯 作业**
1. 阅读Runnable源码
2. 实现自定义Runnable
3. 理解Chain的执行流程

---

### Day 50-51: 源码解读 - LangGraph实现

**📖 理论**
- LangGraph架构
- StateGraph实现
- 节点执行机制
- 检查点系统

**💻 实践**：`week7/day50_source_code_langgraph.py`
- 阅读LangGraph源码
- 理解状态管理
- 自定义节点

**📁 源码学习**
```
源码导读/langgraph/
├── README.md                    # 源码学习指南
├── 01_architecture.md           # 架构概览
├── 02_graph.md                 # Graph实现
├── 03_state.md                 # 状态管理
├── 04_checkpointer.md          # 检查点系统
└── annotated_code/             # 带注释的源码
    ├── graph/
    ├── checkpoint/
    └── pregel/
```

**🎯 作业**
1. 阅读StateGraph源码
2. 实现自定义Checkpointer
3. 理解Pregel算法

---

### Day 52-53: 源码解读 - DeepAgents架构

**📖 理论**
- DeepAgents架构设计
- Agent执行引擎
- Task调度器
- Crew管理器

**💻 实践**：`week7/day52_source_code_deepagents.py`
- 阅读DeepAgents源码
- 理解调度机制
- 自定义Process

**📁 源码学习**
```
源码导读/deepagents/
├── README.md                    # 源码学习指南
├── 01_architecture.md           # 架构概览
├── 02_agent.md                 # Agent实现
├── 03_task.md                  # Task系统
├── 04_crew.md                  # Crew管理
└── annotated_code/             # 带注释的源码
    ├── agent/
    ├── task/
    └── crew/
```

**🎯 作业**
1. 阅读Agent执行源码
2. 实现自定义Process
3. 理解任务调度

---

### Day 54-55: 部署与运维

**📖 理论**
- 部署策略（Docker、K8s）
- API服务化
- 负载均衡
- 备份和恢复

**💻 实践**：`week8/day54_deployment.py`
- Docker化应用
- 创建API服务
- 部署到生产环境

**🎯 作业**
1. 创建Docker镜像
2. 实现API接口
3. 部署到云平台

---

### Day 56-60: 【毕业项目】完整的生产级AI应用

**🎯 项目目标**
自选一个完整的生产级AI应用，例如：
- 智能文档处理平台
- AI代码审查系统
- 智能客服平台
- 内容生成系统
- 知识库问答系统

**📋 项目要求**
- 使用LangChain/LangGraph/DeepAgents
- 完整的功能实现
- 生产级代码质量
- 性能优化
- 监控和日志
- 完整的文档
- 部署到生产环境

**📁 项目结构（示例）**
```
graduation_project/
├── README.md                    # 项目说明
├── ARCHITECTURE.md             # 架构设计
├── requirements.txt            # 依赖
├── docker-compose.yml          # Docker配置
├── .env.example               # 环境变量
├── src/
│   ├── __init__.py
│   ├── agents/                # Agent模块
│   ├── tools/                 # 工具模块
│   ├── graph/                 # LangGraph
│   ├── api/                   # API接口
│   └── utils/                 # 工具函数
├── tests/                     # 测试
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/                      # 文档
│   ├── api.md
│   ├── deployment.md
│   └── user_guide.md
├── scripts/                   # 脚本
│   ├── setup.sh
│   ├── deploy.sh
│   └── backup.sh
└── monitoring/                # 监控
    ├── prometheus.yml
    └── grafana/
```

**✅ 评估标准**
- [ ] 功能完整性（30分）
- [ ] 代码质量（20分）
- [ ] 性能优化（15分）
- [ ] 错误处理（10分）
- [ ] 监控和日志（10分）
- [ ] 文档完善（10分）
- [ ] 创新性（5分）

---

## 📂 课程文件结构

```
learn-langchain/
├── README.md                           # 课程总览
├── CURRICULUM_V3.md                    # 本文件 - 详细课程大纲
├── .env.example                        # 环境变量模板
├── requirements.txt                    # 全局依赖
│
├── week1_langchain_basics/            # Week 1: LangChain基础
│   ├── README.md
│   ├── day1_hello_langchain.py
│   ├── day2_messages.py
│   ├── day3_prompts.py
│   ├── day4_chains.py
│   ├── day5_output_parsers.py
│   ├── day6_rag_basics.py
│   └── project_doc_qa/                # Week 1项目
│
├── week2_agent_tools/                 # Week 2: Agent与工具
│   ├── README.md
│   ├── day8_tools.py
│   ├── day9_agent_basics.py
│   ├── day10_api_integration.py
│   ├── day11_memory.py
│   ├── day12_structured_output.py
│   ├── day13_agent_advanced.py
│   └── project_customer_service/     # Week 2项目
│
├── week3_langgraph_basics/            # Week 3: LangGraph基础
│   ├── README.md
│   ├── day15_stategraph_basics.py
│   ├── day17_routing.py
│   ├── day19_checkpoints.py
│   └── project_code_review/          # Week 3项目
│
├── week4_langgraph_advanced/          # Week 4: LangGraph进阶
│   ├── README.md
│   ├── day22_multi_agent.py
│   ├── day25_middleware.py
│   └── project_content_system/       # Week 4项目
│
├── week5_deepagents_basics/           # Week 5: DeepAgents基础
│   ├── README.md
│   ├── day29_deepagents_intro.py
│   ├── day31_agent_task_crew.py
│   ├── day33_tools_process.py
│   └── project_code_assistant_v1/    # Week 5项目
│
├── week6_deepagents_advanced/         # Week 6: DeepAgents进阶
│   ├── README.md
│   ├── day36_advanced_patterns.py
│   ├── day39_enterprise.py
│   └── project_code_assistant_v2/    # Week 6项目
│
├── week7_production_sourcecode/       # Week 7: 生产实践与源码
│   ├── README.md
│   ├── day43_performance.py
│   ├── day46_monitoring.py
│   ├── day48_source_code_langchain.py
│   ├── day50_source_code_langgraph.py
│   └── day52_source_code_deepagents.py
│
├── week8_deployment/                  # Week 8: 部署与毕业项目
│   ├── README.md
│   ├── day54_deployment.py
│   └── graduation_project/           # 毕业项目模板
│
├── source_code_guide/                 # 源码学习指南
│   ├── README.md                     # 源码学习总览
│   ├── langchain/                    # LangChain源码导读
│   │   ├── README.md
│   │   ├── 01_architecture.md
│   │   ├── 02_runnable.md
│   │   ├── 03_chains.md
│   │   ├── 04_agents.md
│   │   └── annotated_code/          # 带注释的源码
│   ├── langgraph/                    # LangGraph源码导读
│   │   ├── README.md
│   │   ├── 01_architecture.md
│   │   ├── 02_graph.md
│   │   ├── 03_state.md
│   │   ├── 04_checkpointer.md
│   │   └── annotated_code/
│   └── deepagents/                   # DeepAgents源码导读
│       ├── README.md
│       ├── 01_architecture.md
│       ├── 02_agent.md
│       ├── 03_task.md
│       ├── 04_crew.md
│       └── annotated_code/
│
├── docs/                              # 课程文档
│   ├── guides/                       # 指南文档
│   │   ├── environment_setup.md      # 环境搭建
│   │   ├── best_practices.md        # 最佳实践
│   │   ├── troubleshooting.md       # 故障排除
│   │   └── faq.md                   # 常见问题
│   └── references/                   # 参考资料
│       ├── api_reference.md         # API参考
│       ├── glossary.md              # 术语表
│       └── resources.md             # 学习资源
│
└── archive/                           # 归档的旧内容
    ├── old_examples/                 # 旧示例代码
    └── old_docs/                     # 旧文档
```

---

## 🎓 学习建议

### 1. 时间安排
- **每天学习**：2-3小时
- **周末项目**：4-6小时
- **总计**：约120-150小时

### 2. 学习方法
- 📚 **理论先行**：先理解概念
- 💻 **动手实践**：必须运行代码
- 📝 **记录笔记**：整理学习心得
- 🤔 **思考扩展**：完成作业和挑战
- 👥 **交流讨论**：加入社区讨论

### 3. 代码规范
- 遵循PEP 8规范
- 写清晰的注释
- 使用类型提示
- 编写测试用例
- 使用Git版本控制

### 4. 学习检查点

**Week 1检查点**：
- [ ] 能独立创建LangChain应用
- [ ] 理解消息系统和Prompt
- [ ] 会使用Chain和LCEL
- [ ] 完成文档问答项目

**Week 2检查点**：
- [ ] 能创建自定义工具
- [ ] 理解Agent工作原理
- [ ] 会集成外部API
- [ ] 完成客服系统项目

**Week 3-4检查点**：
- [ ] 熟练使用LangGraph
- [ ] 能构建复杂状态图
- [ ] 理解检查点机制
- [ ] 完成两个LangGraph项目

**Week 5-6检查点**：
- [ ] 掌握DeepAgents框架
- [ ] 能构建Multi-Agent系统
- [ ] 实现高级Agent模式
- [ ] 完成代码助手项目

**Week 7-8检查点**：
- [ ] 理解框架源码
- [ ] 能优化和调试应用
- [ ] 会部署生产应用
- [ ] 完成毕业项目

### 5. 进阶方向

完成课程后，可以选择以下方向深入：

**方向1：RAG专家**
- 深入学习向量数据库
- 研究检索优化技术
- 学习文档处理技术
- 构建企业级知识库

**方向2：Agent专家**
- 研究AutoGPT等项目
- 学习Agent规划算法
- 深入Multi-Agent系统
- 构建自主Agent

**方向3：工程化专家**
- 深入性能优化
- 学习大规模部署
- 研究监控和运维
- 构建AI平台

**方向4：开源贡献**
- 参与LangChain开发
- 贡献LangGraph
- 参与社区讨论
- 分享经验和教程

---

## 📚 推荐资源

### 官方文档
- [LangChain官方文档](https://python.langchain.com/)
- [LangGraph文档](https://langchain-ai.github.io/langgraph/)
- [DeepAgents GitHub](https://github.com/deepagents/deepagents)
- [Anthropic文档](https://docs.anthropic.com/)

### 社区资源
- [LangChain Discord](https://discord.gg/langchain)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangChain中文社区](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)

### 课程和教程
- [DeepLearning.AI LangChain Courses](https://www.deeplearning.ai/)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain-cookbook)

### 论文和博客
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [LangChain Blog](https://blog.langchain.dev/)
- [Anthropic Research](https://www.anthropic.com/research)

---

## 💬 获取帮助

### 常见问题
1. **环境配置问题**：查看 `docs/guides/environment_setup.md`
2. **API调用失败**：查看 `docs/guides/troubleshooting.md`
3. **代码报错**：查看 `docs/guides/faq.md`

### 技术支持
- 查阅课程文档
- 搜索GitHub Issues
- 在Discord提问
- 查看Stack Overflow

---

## 📝 版本历史

### v3.0 (2026-03-09)
- 🎉 全新设计的课程体系
- 📚 8周系统化学习路径
- 💻 60+实战代码示例
- 📖 源码解读和注释
- 🚀 6个完整实战项目
- 📁 清晰的文件组织结构

---

**开始学习，成为LangChain专家！** 🚀

记住：**实践是最好的老师**。多写代码，多做项目，多思考！

祝学习愉快！💪
