# LangChain 实战精通课程 🎓

> 🚀 从零基础到源码掌握 - 8周系统学习 LangChain、LangGraph 和 DeepAgents

## ✨ 课程亮点

- ✅ **系统完整**：8周60+课时，覆盖所有核心知识点
- ✅ **项目驱动**：每周一个完整实战项目
- ✅ **理论+实战**：每个知识点都有配套代码
- ✅ **源码解读**：深入理解框架原理
- ✅ **生产就绪**：学习工业级开发技巧

## 📚 课程结构

```
📦 learn-langchain (本项目)
│
├── 📘 Week 1: LangChain 基础
│   ├── Day 1-6: 核心概念与实践
│   └── Day 7: 【项目】智能文档问答助手
│
├── 🤖 Week 2: Agent 与工具
│   ├── Day 8-13: Tools、Agent、Memory
│   └── Day 14: 【项目】智能客服系统
│
├── 🔄 Week 3-4: LangGraph
│   ├── Day 15-21: StateGraph、节点、边、检查点
│   ├── Day 21: 【项目】工作流自动化（代码审查）
│   ├── Day 22-27: Multi-Agent、中间件
│   └── Day 28: 【项目】多Agent内容生成系统
│
├── 🚀 Week 5-6: DeepAgents
│   ├── Day 29-34: Agent、Task、Crew
│   ├── Day 35: 【项目】智能代码助手 v1
│   ├── Day 36-41: 高级模式、企业级功能
│   └── Day 42: 【项目】智能代码助手 v2
│
└── 🏭 Week 7-8: 生产实践与源码
    ├── Day 43-47: 性能优化、监控、调试
    ├── Day 48-53: 源码解读（LangChain/LangGraph/DeepAgents）
    ├── Day 54-55: 部署与运维
    └── Day 56-60: 【毕业项目】生产级AI应用
```

## 🚀 快速开始

### 1. 环境准备

```bash
# 创建虚拟环境（推荐使用 virtualenvwrapper）
mkvirtualenv -p python3.12 langchain-learn

# 或使用 venv
python3.12 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# 安装基础依赖
pip install langchain langchain-anthropic langgraph python-dotenv
```

### 2. 配置 API Key

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的 API Key
# ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**获取 API Key**：
- Anthropic: [console.anthropic.com](https://console.anthropic.com/)
- OpenAI: [platform.openai.com](https://platform.openai.com/)（可选，用于embeddings）

### 3. 运行第一个示例

```bash
# 进入 Week 1 目录
cd week1_langchain_basics

# 运行 Day 1 示例
python day1_hello_langchain.py
```

## 📖 学习路径

### 🎯 路径 1: 完整学习（推荐）

按照Week 1 → Week 2 → ... → Week 8的顺序，系统学习所有内容。

**适合人群**：
- LangChain/AI开发新手
- 希望全面掌握框架的开发者
- 有充足时间（8周）

**时间投入**：每天2-3小时，总计120-150小时

---

### 🚀 路径 2: 快速入门（4周）

只学习Week 1-4的内容，掌握核心功能。

**适合人群**：
- 有Python基础，想快速上手
- 需要快速开发原型
- 时间有限

**时间投入**：每天2-3小时，总计60-80小时

---

### 💡 路径 3: 专项深入

根据需求选择特定主题深入学习。

**Agent专家路径**：Week 2 + Week 3-4 + Week 7（Agent源码）
**DeepAgents专家路径**：Week 1-2（基础）+ Week 5-6 + Week 8（源码）
**生产工程路径**：Week 1-2（基础）+ Week 7-8

---

### 📚 路径 4: 源码研究

已经会使用，想深入理解框架原理。

**学习内容**：
- Week 7-8 的源码解读部分
- [source_code_guide/](./source_code_guide/) 目录

**适合人群**：
- 已有LangChain使用经验
- 想要参与开源贡献
- 需要自定义扩展

---

## 📁 项目结构

```
learn-langchain/
├── README.md                          # 本文件 - 课程总览
├── CURRICULUM_V3.md                   # 完整课程大纲
├── .env.example                       # 环境变量模板
├── requirements.txt                   # 全局依赖
│
├── week1_langchain_basics/           # Week 1: LangChain基础
│   ├── README.md                     # Week 1 说明
│   ├── day1_hello_langchain.py       # Day 1-6 示例代码
│   ├── day2_messages.py
│   ├── ...
│   └── project_doc_qa/               # Week 1 项目
│       ├── README.md
│       ├── main.py
│       └── docs/
│
├── week2_agent_tools/                # Week 2: Agent与工具
│   ├── README.md
│   ├── day8_tools.py
│   ├── ...
│   └── project_customer_service/
│
├── week3_langgraph_basics/           # Week 3: LangGraph基础
├── week4_langgraph_advanced/         # Week 4: LangGraph进阶
├── week5_deepagents_basics/          # Week 5: DeepAgents基础
├── week6_deepagents_advanced/        # Week 6: DeepAgents进阶
├── week7_production_sourcecode/      # Week 7: 生产实践与源码
├── week8_deployment/                 # Week 8: 部署与毕业项目
│
├── source_code_guide/                # 源码学习指南
│   ├── README.md                     # 源码学习总览
│   ├── langchain/                    # LangChain源码导读
│   ├── langgraph/                    # LangGraph源码导读
│   └── deepagents/                   # DeepAgents源码导读
│
├── docs/                             # 课程文档
│   ├── guides/                       # 使用指南
│   └── references/                   # 参考资料
│
└── archive/                          # 旧内容归档
```

## 🎯 学习目标

完成本课程后，你将能够：

### 基础能力（Week 1-2）
- ✅ 熟练使用 LangChain 开发 AI 应用
- ✅ 创建和管理 Agent 和 Tools
- ✅ 实现对话记忆和上下文管理
- ✅ 集成外部 API 和数据源

### 进阶能力（Week 3-6）
- ✅ 使用 LangGraph 构建复杂工作流
- ✅ 实现 Multi-Agent 协作系统
- ✅ 掌握 DeepAgents 框架
- ✅ 构建企业级 AI 应用

### 专家能力（Week 7-8）
- ✅ 优化性能和控制成本
- ✅ 深入理解框架源码和原理
- ✅ 部署和维护生产环境
- ✅ 自定义扩展和贡献开源

## 📚 核心文档

### 🌟 必读文档

1. **[CURRICULUM_V3.md](./CURRICULUM_V3.md)** ⭐⭐⭐
   - 完整的8周课程大纲
   - 每日学习目标和内容
   - 实践任务和作业
   - 项目详细说明

2. **[source_code_guide/README.md](./source_code_guide/README.md)** ⭐⭐⭐
   - 源码学习指南
   - LangChain/LangGraph/DeepAgents源码导读
   - 架构设计和实现原理

### 📖 每周文档

每个week目录下都有README.md，包含：
- 本周学习目标
- 每日学习内容
- 示例代码说明
- 作业和项目要求

### 📘 辅助文档

- [docs/guides/environment_setup.md](./docs/guides/environment_setup.md) - 环境搭建指南
- [docs/guides/best_practices.md](./docs/guides/best_practices.md) - 最佳实践
- [docs/guides/troubleshooting.md](./docs/guides/troubleshooting.md) - 故障排除
- [docs/guides/faq.md](./docs/guides/faq.md) - 常见问题

## 🎓 6个实战项目

### 1. 智能文档问答助手（Week 1）
构建一个能理解和回答文档内容的AI助手。

**技术栈**：LangChain基础、Prompt工程、文档加载

---

### 2. 智能客服系统（Week 2）
实现一个完整的客服机器人，支持多意图识别和工具调用。

**技术栈**：Agent、Tools、Memory、结构化输出

---

### 3. 工作流自动化 - 代码审查（Week 3）
自动化代码审查流程，检测问题并生成报告。

**技术栈**：LangGraph、StateGraph、条件路由

---

### 4. 多Agent内容生成系统（Week 4）
多个Agent协作完成内容研究、撰写、编辑和优化。

**技术栈**：Multi-Agent、LangGraph进阶、中间件

---

### 5. 智能代码助手（Week 5-6）
完整的代码分析、Bug检测、重构建议、测试生成系统。

**技术栈**：DeepAgents、Agent、Task、Crew、高级模式

---

### 6. 毕业项目：生产级AI应用（Week 8）
自选主题，构建一个完整的生产级应用。

**要求**：功能完整、性能优化、监控日志、部署文档

---

## 💻 技术栈

- **Python**: 3.11+ （推荐 3.12）
- **核心框架**:
  - LangChain: 最新版本
  - LangGraph: 最新版本  
  - DeepAgents: 最新版本
- **LLM 提供商**:
  - Anthropic Claude（推荐，主要使用）
  - OpenAI GPT（可选，用于embeddings）
- **开发工具**:
  - virtualenvwrapper 或 venv
  - python-dotenv
  - LangSmith（可选，用于监控）

## 📝 学习建议

### 1. 时间管理
- **每天学习**：2-3小时
- **周末项目**：4-6小时
- **总计**：约120-150小时（8周）

### 2. 学习方法
- 📚 **理论先行**：先理解概念
- 💻 **动手实践**：必须运行代码
- 📝 **记录笔记**：整理学习心得
- 🤔 **完成作业**：加深理解
- 👥 **交流讨论**：加入社区

### 3. 代码规范
- 遵循 PEP 8 规范
- 写清晰的注释
- 使用类型提示
- 编写测试用例
- 使用 Git 版本控制

### 4. 学习检查点

完成每周后，检查是否达到目标：

**Week 1 ✓**：
- [ ] 能独立创建LangChain应用
- [ ] 理解消息系统和Prompt
- [ ] 会使用Chain和LCEL
- [ ] 完成文档问答项目

**Week 2 ✓**：
- [ ] 能创建自定义工具
- [ ] 理解Agent工作原理
- [ ] 会集成外部API
- [ ] 完成客服系统项目

**Week 3-4 ✓**：
- [ ] 熟练使用LangGraph
- [ ] 能构建复杂状态图
- [ ] 理解检查点机制
- [ ] 完成两个LangGraph项目

**Week 5-6 ✓**：
- [ ] 掌握DeepAgents框架
- [ ] 能构建Multi-Agent系统
- [ ] 实现高级Agent模式
- [ ] 完成代码助手项目

**Week 7-8 ✓**：
- [ ] 理解框架源码
- [ ] 能优化和调试应用
- [ ] 会部署生产应用
- [ ] 完成毕业项目

## 🔗 官方资源

### 核心文档
- [LangChain官方文档](https://python.langchain.com/)
- [LangGraph文档](https://langchain-ai.github.io/langgraph/)
- [DeepAgents GitHub](https://github.com/deepagents/deepagents)
- [Anthropic文档](https://docs.anthropic.com/)

### GitHub 仓库
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [DeepAgents GitHub](https://github.com/deepagents/deepagents)

### 社区资源
- [LangChain Discord](https://discord.gg/langchain)
- [LangChain Twitter](https://twitter.com/langchainai)
- [DeepLearning.AI Courses](https://www.deeplearning.ai/)

## ❓ 常见问题

### Q1: 需要什么基础？
**A**: 需要：
- Python编程基础（语法、面向对象、异常处理）
- 基本的命令行操作
- 了解REST API概念（加分项）

不需要：
- 机器学习/深度学习经验
- 前端开发经验

---

### Q2: 学完需要多久？
**A**: 
- **完整学习**：8周（每天2-3小时）
- **快速入门**：4周（前4周内容）
- **专项深入**：根据主题，2-4周

---

### Q3: 遇到问题怎么办？
**A**:
1. 查看课程文档和FAQ
2. 搜索GitHub Issues
3. 在Discord/社区提问
4. 查阅官方文档

---

### Q4: API调用会花费多少？
**A**:
- 学习阶段使用Claude 3.5 Sonnet，成本约$10-20
- 可以使用Haiku模型降低成本
- Anthropic新用户有免费额度

---

### Q5: 需要GPU吗？
**A**: 
不需要！我们使用的是API方式调用LLM，所有计算都在云端完成。

---

## 🎉 开始学习

### 推荐起点

**1. 新手入门**
```bash
# 从 Week 1 Day 1 开始
cd week1_langchain_basics
python day1_hello_langchain.py
```

**2. 有经验的开发者**
```bash
# 先浏览完整大纲
cat CURRICULUM_V3.md

# 然后选择感兴趣的主题
cd week3_langgraph_basics  # 或其他week
```

**3. 源码研究者**
```bash
# 直接进入源码学习
cd source_code_guide
cat README.md
```

---

## 📊 课程版本

**当前版本**: v3.0 (2026-03-09)

**更新内容**：
- 🎉 全新设计的课程体系
- 📚 8周系统化学习路径
- 💻 60+实战代码示例
- 📖 源码解读和注释
- 🚀 6个完整实战项目
- 📁 清晰的文件组织结构

---

## 💪 加入我们

### 贡献指南
欢迎贡献代码、修复错误、改进文档！

### 反馈建议
遇到问题或有改进建议？请提交Issue。

### 分享经验
完成课程后，欢迎分享你的学习心得和项目！

---

**🚀 准备好了吗？让我们开始这段精彩的学习之旅！**

记住：**实践是最好的老师**。多写代码，多做项目，多思考！

祝学习愉快！💪
