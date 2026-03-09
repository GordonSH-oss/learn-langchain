# LangChain 精通计划 - Week 2-8 概览

> 本文档是 `CURRICULUM_MASTER.md` 的补充，涵盖 Week 2-8 的详细内容

## 📚 课程结构

```
Week 2: Agent 基础和 Tools 系统
Week 3-4: LangGraph 核心和状态管理  
Week 5-6: DeepAgents 和多 Agent 系统
Week 7-8: 生产实践和性能优化
```

---

## 🤖 Week 2：Agent 基础和 Tools 系统（Day 8-14）

### Day 8：Tools（工具）系统基础

**学习目标**：
- 理解 Tools 的概念和作用
- 学会创建自定义工具
- 掌握工具的参数和返回值

**核心内容**：
1. 什么是 Tool
2. Tool 的组成部分：
   - name: 工具名称
   - description: 工具描述（给 LLM 看的）
   - function: 实际执行的函数
   - args_schema: 参数定义

3. 创建 Tool 的方式：
   - @tool 装饰器
   - StructuredTool.from_function()
   - 自定义 BaseTool 子类

**实践**：
```bash
# 参考示例
python examples/use-agent-tool.py
python examples/use-agent-tool-real-weather.py
```

**作业**：
创建以下工具：
1. 计算器工具（支持加减乘除）
2. 文件读写工具
3. 网页抓取工具
4. 时间转换工具

---

### Day 9：集成真实 API

**学习目标**：
- 学习 API 集成模式
- 处理 API 认证
- 错误处理和重试

**实践内容**：
1. 集成天气 API
2. 集成搜索 API
3. 集成数据库查询
4. 实现 API 缓存

**参考文档**：
- `docs/guides/WEATHER_API_GUIDE.md`

---

### Day 10-11：Agent 创建和配置

**学习目标**：
- 深入理解 create_agent
- 掌握 Agent 的配置参数
- 理解 ReAct 模式

**核心知识**：
1. Agent 类型：
   - ReAct Agent
   - OpenAI Functions Agent  
   - Structured Chat Agent
   - Custom Agent

2. create_agent 参数详解：
   - model: 使用的模型
   - tools: 工具列表
   - system_prompt: 系统提示词
   - state_schema: 状态模式
   - checkpointer: 检查点管理器

**深入研究**：
- `docs/advanced/create-agent-analysis.md`
- `docs/advanced/tool-strategy-analysis.md`

---

### Day 12：记忆系统（Memory）

**学习目标**：
- 理解记忆的作用
- 掌握不同的记忆类型
- 实现持久化记忆

**记忆类型**：
1. ConversationBufferMemory - 缓冲记忆
2. ConversationSummaryMemory - 摘要记忆
3. ConversationBufferWindowMemory - 窗口记忆
4. VectorStoreMemory - 向量存储记忆

**实践**：
```bash
python examples/use-agent-with-memory-1.py
python examples/use-agent-with-memory-improved.py
python examples/use-agent-with-memory-realistic.py  # 重点
```

**参考文档**：
- `docs/guides/HOW_TO_FILL_USER_INFO.md`

---

### Day 13：结构化输出

**学习目标**：
- 深入理解 ToolStrategy 和 ProviderStrategy
- 实现复杂的结构化输出
- 处理输出验证

**深入内容**：
- Union 类型处理
- 嵌套结构
- 错误处理和重试
- 自定义验证逻辑

**参考文档**：
- `docs/advanced/tool-strategy-analysis.md`

---

### Day 14：Week 2 项目 - 智能客服系统

**项目目标**：
构建一个完整的智能客服系统

**功能需求**：
1. 多工具支持：
   - 订单查询
   - 物流追踪
   - FAQ 问答
   - 人工转接

2. 记忆管理：
   - 用户会话管理
   - 对话历史持久化
   - 上下文理解

3. 结构化输出：
   - 订单信息
   - 物流信息
   - 意图识别结果

---

## 🔄 Week 3-4：LangGraph 核心（Day 15-28）

### Week 3 核心内容

#### Day 15-16：StateGraph 基础

**学习目标**：
- 理解状态图的概念
- 掌握 StateGraph API
- 创建第一个状态图

**核心概念**：
1. State（状态）
2. Node（节点）
3. Edge（边）
4. Conditional Edge（条件边）

**实践**：
```bash
python examples/use-agent-anthropic-langgraph.py
```

---

#### Day 17-18：节点和边

**学习内容**：
1. 节点类型：
   - 函数节点
   - ToolNode
   - LLM 节点
   - 自定义节点

2. 边的类型：
   - 普通边（add_edge）
   - 条件边（add_conditional_edges）
   - 起始边（set_entry_point）
   - 结束边（END）

3. 路由逻辑：
   - 基于状态的路由
   - 基于输出的路由
   - 复杂路由条件

---

#### Day 19-21：检查点和持久化

**学习内容**：
1. Checkpointer 概念
2. MemorySaver vs SqliteSaver
3. 状态恢复
4. 断点续传
5. 时间旅行调试

**进阶内容**：
- Store 跨线程存储
- Interrupt 中断机制
- Human-in-the-loop

---

### Week 4 高级特性

#### Day 22-24：高级 Agent 模式

**学习内容**：
1. Multi-Agent 协作
2. Supervisor Pattern
3. Handoff Pattern  
4. Hierarchical Agent

**实践项目**：
构建多 Agent 协作系统

---

#### Day 25-27：中间件和扩展

**学习内容**：
1. AgentMiddleware
2. 自定义 State Schema
3. Runtime Context
4. 钩子函数

**参考文档**：
- `docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md`

---

#### Day 28：Week 3-4 项目 - 工作流自动化系统

**项目内容**：
构建一个复杂的工作流自动化系统，如：
- 代码审查助手
- 数据分析 Pipeline
- 内容生成工作流

---

## 🚀 Week 5-6：DeepAgents 和高级应用（Day 29-42）

### Week 5：DeepAgents 入门

#### Day 29-30：DeepAgents 架构

**学习目标**：
- 理解 DeepAgents 框架
- 掌握核心 API
- 了解与 LangChain 的关系

**环境准备**：
```bash
workon langchain  # 或者你的环境
pip install deepagents
```

**核心概念**：
1. DeepAgents 是什么
2. 与 LangChain/LangGraph 的区别
3. 适用场景

---

#### Day 31-33：DeepAgents 核心功能

**学习内容**：
1. Agent 创建和配置
2. 工具系统
3. 记忆管理
4. 状态管理

**实践**：
阅读并运行 `deepagents/README.md` 中的示例

---

#### Day 34-35：多 Agent 系统

**学习内容**：
1. Agent 间通信
2. 任务分配和协作
3. 冲突解决
4. 性能优化

---

### Week 6：生产级 Agent 开发

#### Day 36-38：企业级功能

**学习内容**：
1. 安全性和权限控制
2. 监控和日志
3. 错误处理和恢复
4. 性能监控

---

#### Day 39-41：高级模式

**学习内容**：
1. Planning Pattern
2. Reflection Pattern
3. Self-improvement Pattern
4. Meta-Agent Pattern

---

#### Day 42：Week 5-6 项目 - 智能代码助手

**项目目标**：
构建一个智能代码助手，具备：
1. 代码理解和分析
2. Bug 检测和修复建议
3. 代码重构建议
4. 测试用例生成
5. 文档自动生成

---

## 🏭 Week 7-8：生产实践和优化（Day 43-60）

### Week 7：性能优化和最佳实践

#### Day 43-45：性能优化

**优化方向**：
1. **Prompt 优化**：
   - 减少 token 使用
   - 提高响应质量
   - 缓存策略

2. **并发处理**：
   - 异步调用
   - 批处理
   - 连接池

3. **缓存机制**：
   - LLM 响应缓存
   - Embedding 缓存
   - 结果缓存

---

#### Day 46-48：监控和调试

**学习内容**：
1. LangSmith 集成
2. 日志系统
3. 性能监控
4. 错误追踪
5. A/B 测试

---

#### Day 49：错误处理和容错

**学习内容**：
1. 重试机制
2. Fallback 策略
3. Circuit Breaker
4. 优雅降级

---

### Week 8：部署和维护

#### Day 50-52：部署策略

**学习内容**：
1. **容器化部署**：
   - Docker
   - Docker Compose
   - Kubernetes

2. **云平台部署**：
   - AWS Lambda
   - Google Cloud Run
   - Azure Functions

3. **API 服务**：
   - FastAPI
   - Flask
   - Serverless

---

#### Day 53-55：安全和合规

**学习内容**：
1. API Key 管理
2. 数据安全
3. 用户隐私
4. 审计日志
5. 合规要求

---

#### Day 56-57：成本优化

**学习内容**：
1. Token 使用优化
2. 模型选择策略
3. 缓存最大化
4. 批处理优化
5. 成本监控

---

#### Day 58-60：毕业项目 - 完整的 AI 应用

**项目要求**：
设计并实现一个完整的生产级 AI 应用，包含：

1. **功能完整**：
   - 核心功能实现
   - 用户界面（Web/CLI/API）
   - 数据持久化
   - 用户管理

2. **性能优良**：
   - 响应时间 < 3s
   - 支持并发
   - 资源优化

3. **可维护性**：
   - 代码规范
   - 文档完善
   - 测试覆盖
   - CI/CD

4. **部署就绪**：
   - Docker 化
   - 环境配置
   - 监控告警
   - 日志系统

**推荐项目方向**：
- 智能文档分析系统
- AI 代码审查平台
- 智能客服系统
- 内容生成平台
- 数据分析助手

---

## 📊 学习评估

### Week 2 评估
- [ ] 能独立创建和集成工具
- [ ] 理解 Agent 的工作原理
- [ ] 实现完整的记忆管理
- [ ] 完成智能客服项目

### Week 3-4 评估  
- [ ] 熟练使用 StateGraph
- [ ] 理解检查点机制
- [ ] 能设计复杂工作流
- [ ] 完成工作流项目

### Week 5-6 评估
- [ ] 掌握 DeepAgents 框架
- [ ] 能构建多 Agent 系统
- [ ] 理解高级模式
- [ ] 完成代码助手项目

### Week 7-8 评估
- [ ] 能优化 Agent 性能
- [ ] 能部署生产应用
- [ ] 理解安全和成本
- [ ] 完成毕业项目

---

## 🎓 进阶方向

完成 60 天课程后，可以继续学习：

1. **RAG 深入**：
   - 高级检索策略
   - Reranking
   - Hybrid Search
   - 知识图谱

2. **Fine-tuning**：
   - 模型微调
   - RLHF
   - Few-shot Learning

3. **多模态**：
   - 图像理解
   - 语音识别
   - 视频分析

4. **开源贡献**：
   - 为 LangChain 贡献代码
   - 创建自己的 Agent 框架
   - 分享最佳实践

---

## 💡 学习资源

### 在线资源
- LangChain Academy
- DeepLearning.AI Courses
- YouTube 教程

### 书籍推荐
- "Building LLM Applications"
- "AI Engineering Handbook"
- "Designing Data-Intensive Applications"

### 社区
- LangChain Discord
- Reddit r/LangChain
- GitHub Discussions

---

**继续精进，成为 LangChain 专家！** 🚀
