# Week 1: LangChain 基础

> 从零开始学习 LangChain 核心概念

## 📚 本周学习目标

- 搭建开发环境，运行第一个LangChain应用
- 理解LLM调用、消息系统、Prompt工程
- 掌握Chain组合和LCEL语法
- 学会使用输出解析器
- 了解文档加载和RAG基础
- **项目**：构建智能文档问答助手

## 📅 学习计划

- **Day 1**: 环境搭建 & 第一个应用
- **Day 2**: LLM调用与消息系统
- **Day 3**: Prompt工程与模板
- **Day 4**: Chain与LCEL
- **Day 5**: 输出解析器
- **Day 6**: 文档加载与RAG基础
- **Day 7**: 【项目】智能文档问答助手

## 🚀 快速开始

```bash
# 1. 进入Week 1目录
cd week1_langchain_basics

# 2. 确保已安装依赖（在项目根目录）
pip install langchain langchain-anthropic python-dotenv

# 3. 配置环境变量（在项目根目录）
# 编辑 .env 文件，填入 ANTHROPIC_API_KEY

# 4. 运行Day 1示例
python day1_hello_langchain.py
```

## 📖 每日学习内容

### Day 1: 环境搭建 & 第一个应用

**文件**: `day1_hello_langchain.py`

**学习内容**:
- LangChain生态系统概览
- 核心组件介绍
- 第一个LLM调用
- 基础的问答系统

**作业**:
1. 成功运行示例代码
2. 修改system_prompt，创建不同性格的AI助手
3. 实现一个简单的翻译助手

---

### Day 2: LLM调用与消息系统

**文件**: `day2_messages.py`

**学习内容**:
- Message类型详解
- 对话历史管理
- 参数调优（temperature等）
- Token管理

**作业**:
1. 实现一个记录对话历史的聊天机器人
2. 测试不同temperature值对输出的影响
3. 实现token计数和限制

---

### Day 3: Prompt工程与模板

**文件**: `day3_prompts.py`

**学习内容**:
- Prompt工程最佳实践
- PromptTemplate使用
- Few-shot学习
- ChatPromptTemplate

**作业**:
1. 创建一个代码生成的Prompt模板
2. 实现Few-shot分类器
3. 设计一个SQL生成助手的Prompt

---

### Day 4: Chain与LCEL

**文件**: `day4_chains.py`

**学习内容**:
- Chain的概念和类型
- LCEL语法
- 链式调用与组合
- 管道操作符使用

**作业**:
1. 创建一个"分析-总结-评分"的Chain
2. 用LCEL实现复杂的数据处理流程
3. 实现一个文章改写Chain

---

### Day 5: 输出解析器

**文件**: `day5_output_parsers.py`

**学习内容**:
- StructuredOutputParser
- Pydantic OutputParser
- JSON输出解析
- 错误处理

**作业**:
1. 创建一个返回结构化数据的系统
2. 实现数据验证和错误处理
3. 设计一个产品信息提取器

---

### Day 6: 文档加载与RAG基础

**文件**: `day6_rag_basics.py`

**学习内容**:
- DocumentLoader概念
- 文本分割策略
- 向量数据库基础
- RAG简介

**作业**:
1. 加载并处理自己的文档
2. 实现不同的分割策略对比
3. 构建基础的文档检索系统

---

### Day 7: 【项目】智能文档问答助手

**目录**: `project_doc_qa/`

**项目目标**:
构建一个完整的文档问答系统，支持：
- 上传多种格式文档
- 智能分割和索引
- 基于上下文的问答
- CLI交互界面

**评估标准**:
- [ ] 成功加载和处理文档
- [ ] 准确回答基于文档的问题
- [ ] 引用来源信息
- [ ] 友好的用户界面
- [ ] 代码规范和注释

---

## 📝 学习建议

1. **循序渐进**: 按照Day 1到Day 7的顺序学习
2. **动手实践**: 每个示例都要运行并理解
3. **完成作业**: 作业能加深理解
4. **记录笔记**: 整理学习心得
5. **准备项目**: Day 7之前复习前6天内容

## 💡 常见问题

### Q1: 运行报错怎么办？
- 确保已安装所有依赖
- 检查 .env 文件配置
- 查看错误信息，定位问题

### Q2: API调用失败？
- 验证API Key是否正确
- 检查网络连接
- 查看API余额

### Q3: 示例代码看不懂？
- 先看代码注释
- 查阅LangChain官方文档
- 在社区提问

## 🔗 相关资源

- [LangChain官方文档](https://python.langchain.com/)
- [Anthropic文档](https://docs.anthropic.com/)
- [课程总大纲](../CURRICULUM_V3.md)

---

**准备好了吗？让我们从Day 1开始！** 🚀
