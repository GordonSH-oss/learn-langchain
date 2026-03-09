# 快速导航 - 如何使用这套教程

> 5分钟了解如何开始学习，选择适合你的学习路径

## 🎯 我该从哪里开始？

### 情况 1: 我是完全的新手，从未接触过 LangChain

**推荐路径**：60天精通计划（从头开始）

```
第1步：阅读 README.md（你现在的位置）
   ↓
第2步：配置开发环境（5分钟）
   ├── 安装 Python 3.12
   ├── 创建虚拟环境
   └── 安装依赖包
   ↓
第3步：打开 CURRICULUM_MASTER.md
   ├── 阅读课程目标和结构
   └── 从 Day 1 开始学习
   ↓
第4步：每天学习 2-3 小时
   ├── 阅读当天的学习内容
   ├── 运行代码示例
   ├── 完成实践任务
   └── 完成作业
   ↓
第5步：周末做项目
   └── 巩固本周所学
```

**预计时间**：60 天（每天 2-3 小时）

**学习文档顺序**：
1. `README.md` - 总览（✅ 现在）
2. `CURRICULUM_MASTER.md` - Day 1-7
3. `CURRICULUM_WEEK2-8.md` - Day 8-60
4. `DEEPAGENTS_GUIDE.md` - Week 5-6 重点学习

---

### 情况 2: 我学过 LangChain 基础，想深入学习

**推荐路径**：从 LangGraph 开始（Week 3）

```
第1步：快速复习（1-2天）
   ├── 浏览 CURRICULUM_MASTER.md Week 1
   └── 确认掌握基础概念
   ↓
第2步：学习 LangGraph（Week 3-4）
   └── 阅读 CURRICULUM_WEEK2-8.md Week 3-4 部分
   ↓
第3步：学习 DeepAgents（Week 5-6）
   └── 阅读 DEEPAGENTS_GUIDE.md
   ↓
第4步：生产实践（Week 7-8）
   └── 阅读 CURRICULUM_WEEK2-8.md Week 7-8 部分
```

**预计时间**：30-40 天

---

### 情况 3: 我只想学习 DeepAgents

**推荐路径**：DeepAgents 专项学习

```
前置要求检查：
   ├── ✅ 熟悉 Python 编程
   ├── ✅ 了解 LangChain 基础（LLM、Prompt、Chain）
   └── ✅ 知道什么是 Agent 和 Tools
   ↓
如果前置要求不满足：
   └── 先学习 CURRICULUM_MASTER.md Week 1-2
   ↓
直接学习 DeepAgents：
   ├── 打开 DEEPAGENTS_GUIDE.md
   ├── 从"快速开始"部分开始
   ├── 完成所有教程（教程 1-4）
   ├── 学习高级特性
   └── 完成 3 个实战项目
```

**预计时间**：10-14 天

---

### 情况 4: 我要准备生产部署

**推荐路径**：生产实践专项

```
第1步：性能优化（Week 7 前半部分）
   └── CURRICULUM_WEEK2-8.md Day 43-45
   ↓
第2步：监控和调试（Week 7 后半部分）
   └── CURRICULUM_WEEK2-8.md Day 46-49
   ↓
第3步：部署和安全（Week 8）
   └── CURRICULUM_WEEK2-8.md Day 50-57
   ↓
第4步：实践项目
   └── 将你的项目改造为生产级
```

**预计时间**：7-14 天

---

## 📚 文档导航图

```
README.md (总入口)
    │
    ├─── 🌟 核心学习路径
    │    │
    │    ├─ CURRICULUM_MASTER.md (主课程)
    │    │   ├── 课程目标和结构
    │    │   ├── Week 1: LangChain 基础
    │    │   │   ├── Day 1: 环境搭建
    │    │   │   ├── Day 2: 消息系统
    │    │   │   ├── Day 3: Prompt 工程
    │    │   │   ├── Day 4: Chain 和 LCEL
    │    │   │   ├── Day 5: 输出解析器
    │    │   │   ├── Day 6: RAG 基础
    │    │   │   └── Day 7: 项目 - 文档助手
    │    │   └── 补充资源
    │    │
    │    ├─ CURRICULUM_WEEK2-8.md (后续课程)
    │    │   ├── Week 2: Agent 和 Tools
    │    │   ├── Week 3-4: LangGraph
    │    │   ├── Week 5-6: DeepAgents
    │    │   └── Week 7-8: 生产实践
    │    │
    │    └─ DEEPAGENTS_GUIDE.md (专题)
    │        ├── 概述和快速开始
    │        ├── 核心概念
    │        ├── 深入教程（4个）
    │        ├── 高级特性
    │        ├── 实战项目（3个）
    │        └── 最佳实践
    │
    ├─── 📖 原有文档（仍然有效）
    │    ├── CURRICULUM.md (原30天计划)
    │    └── learn-langchain/
    │        ├── README.md
    │        ├── ANTHROPIC_AGENT_README.md
    │        ├── docs/guides/
    │        └── docs/advanced/
    │
    └─── 💻 示例代码
         └── learn-langchain/examples/
             ├── use-agent-anthropic-*.py
             ├── use-agent-tool-*.py
             └── use-agent-with-memory-*.py
```

---

## 📖 文档快速索引

### 必读文档（按优先级）

#### 🌟 Level 1 - 入门必读
1. **README.md** - 项目总览
2. **QUICK_START.md** - 本文档，快速导航

#### 🌟 Level 2 - 核心学习
3. **CURRICULUM_MASTER.md** - 60天主课程（⭐⭐⭐）
4. **CURRICULUM_WEEK2-8.md** - Week 2-8 内容（⭐⭐⭐）
5. **DEEPAGENTS_GUIDE.md** - DeepAgents 专题（⭐⭐⭐）

#### 📚 Level 3 - 参考文档
6. **CURRICULUM.md** - 原30天计划
7. **learn-langchain/README.md** - 项目说明
8. **UPDATE_SUMMARY.md** - 更新说明

#### 🎓 Level 4 - 进阶文档
9. **learn-langchain/docs/guides/** - 使用指南
10. **learn-langchain/docs/advanced/** - 进阶文档

---

## 💡 学习建议

### 时间规划建议

**全职学习（每天 6-8 小时）**：
- Week 1-2: LangChain 基础（可以加速，1周完成）
- Week 3-4: LangGraph（可以加速，1周完成）
- Week 5-6: DeepAgents（2周）
- Week 7-8: 生产实践（2周）
- **总计：6周（42天）**

**兼职学习（每天 2-3 小时）**：
- Week 1-2: LangChain 基础（2周）
- Week 3-4: LangGraph（2周）
- Week 5-6: DeepAgents（2周）
- Week 7-8: 生产实践（2周）
- **总计：8周（60天）**

**周末学习（每周末 8-10 小时）**：
- Week 1-4: LangChain + LangGraph（4周）
- Week 5-8: DeepAgents（4周）
- Week 9-12: 生产实践（4周）
- **总计：12周（84天）**

### 学习方法建议

1. **理论与实践结合**
   - 40% 时间看文档
   - 60% 时间写代码

2. **循序渐进**
   - 不要跳跃
   - 打好基础再进阶

3. **记录笔记**
   - 重点概念
   - 遇到的问题
   - 解决方案

4. **做项目**
   - 每周的项目必须完成
   - 可以根据兴趣调整项目内容

5. **寻求帮助**
   - 遇到问题先搜索
   - 再问社区
   - 最后查看源码

---

## 🎯 学习检查清单

### Week 1 结束时
- [ ] 能运行第一个 LangChain 程序
- [ ] 理解 LLM、Prompt、Chain 概念
- [ ] 会创建多轮对话
- [ ] 会使用 PromptTemplate
- [ ] 理解 LCEL 语法
- [ ] 会使用输出解析器
- [ ] 了解 RAG 基础
- [ ] 完成文档助手项目

### Week 2 结束时
- [ ] 会创建自定义工具
- [ ] 能集成外部 API
- [ ] 理解 Agent 工作原理
- [ ] 会实现记忆管理
- [ ] 掌握结构化输出
- [ ] 完成客服系统项目

### Week 4 结束时
- [ ] 熟练使用 StateGraph
- [ ] 理解节点和边
- [ ] 会实现条件路由
- [ ] 掌握检查点机制
- [ ] 能构建多 Agent 系统
- [ ] 完成工作流项目

### Week 6 结束时
- [ ] 理解 DeepAgents 架构
- [ ] 会创建 Agent、Task、Crew
- [ ] 掌握层级协作模式
- [ ] 了解高级 Agent 模式
- [ ] 完成代码助手项目

### Week 8 结束时
- [ ] 能优化 Agent 性能
- [ ] 会实现监控和日志
- [ ] 了解部署策略
- [ ] 理解安全和成本
- [ ] 完成毕业项目

---

## ❓ 常见问题

### Q1: 我需要什么基础？
**A**: 
- 必需：Python 基础（函数、类、异步）
- 推荐：了解 REST API、JSON
- 加分：机器学习基础知识

### Q2: 需要什么硬件？
**A**: 
- 能运行 Python 的电脑即可
- 不需要 GPU（使用云端 API）
- 推荐 8GB+ 内存

### Q3: 费用多少？
**A**: 
- 课程：免费
- API 费用：每月 $10-50（取决于使用量）
- 推荐：先用 Anthropic 的免费额度

### Q4: 英语不好可以学吗？
**A**: 
- 教程是中文的 ✅
- 官方文档是英文的（可以翻译）
- 代码注释是中文的 ✅

### Q5: 学完能做什么？
**A**: 
- 开发 AI 应用
- 构建智能客服
- 创建内容生成工具
- 数据分析助手
- 代码审查工具

### Q6: 卡住了怎么办？
**A**: 
1. 重新阅读相关章节
2. 查看示例代码
3. 搜索错误信息
4. 在社区提问
5. 查看官方文档

---

## 🚀 立即开始

准备好了吗？让我们开始吧！

### 第一步：配置环境（5分钟）

```bash
# 1. 创建虚拟环境
mkvirtualenv -p python3.12 langchain-master

# 2. 克隆或下载项目
cd /path/to/your/workspace

# 3. 安装依赖
pip install langchain langchain-anthropic langgraph deepagents python-dotenv

# 4. 配置 API Key
cd learn-langchain
cp .env.example .env
# 编辑 .env，填入你的 ANTHROPIC_API_KEY
```

### 第二步：运行第一个示例（1分钟）

```bash
python examples/use-agent-anthropic-qa-only.py
```

### 第三步：开始系统学习

打开 **CURRICULUM_MASTER.md**，从 Day 1 开始！

---

## 📞 需要帮助？

- 📚 查看 [README.md](./README.md)
- 💬 加入 LangChain Discord
- 🐛 提交 GitHub Issue
- 📖 查看官方文档

---

**记住：最重要的是开始行动！**

不要被 60 天吓到，一步一步来，你一定可以的！💪

祝学习愉快！🎉

---

*快速导航 - 最后更新: 2026-03-04*
