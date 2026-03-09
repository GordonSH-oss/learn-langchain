# 🚀 快速导航 - 5分钟选择你的学习路径

> 不知道从哪开始？这个文档帮你快速找到适合的学习路径！

## 🎯 你是哪种情况？

### 情况 1: 完全新手，没用过 LangChain
**推荐路径**: 🔰 完整学习路径

**从这里开始**:
```bash
cd week1_langchain_basics
python day1_hello_langchain.py
```

**学习安排**:
- Week 1-2: 基础（2周）
- Week 3-4: LangGraph（2周）
- Week 5-6: DeepAgents（2周）
- Week 7-8: 生产实践（2周）

**预计时间**: 8周，每天2-3小时

---

### 情况 2: 会Python，想快速上手 LangChain
**推荐路径**: 🚀 快速入门路径

**从这里开始**:
```bash
# Day 1: 第一个应用
cd week1_langchain_basics
python day1_hello_langchain.py

# Day 2-3: Agent 和 Tools
cd ../week2_agent_tools
python day8_tools.py
python day9_agent_basics.py
```

**学习安排**:
- Week 1: LangChain基础（快速过）
- Week 2: Agent和Tools（重点）
- Week 3-4: LangGraph（选学）

**预计时间**: 2-4周，每天2-3小时

---

### 情况 3: 已会用 LangChain，想深入原理
**推荐路径**: 📚 源码研究路径

**从这里开始**:
```bash
cd source_code_guide
cat README.md
cat langchain/01_architecture.md
```

**学习安排**:
- 直接学习 Week 7-8 内容
- 阅读源码导读
- 实现自定义组件

**预计时间**: 1-2周

---

### 情况 4: 想专门学习某个主题

#### 🎯 专注 Agent 开发
```bash
# Week 2: Agent 基础
cd week2_agent_tools

# Week 3-4: LangGraph（Multi-Agent）
cd week3_langgraph_basics
cd week4_langgraph_advanced
```

#### 🤖 专注 DeepAgents
```bash
# Week 1-2: 基础（快速过）
# Week 5-6: DeepAgents（重点）
cd week5_deepagents_basics
cd week6_deepagents_advanced
```

#### 🏭 专注生产部署
```bash
# Week 1-2: 基础（快速过）
# Week 7-8: 生产实践（重点）
cd week7_production_sourcecode
cd week8_deployment
```

---

## 📚 每周详细内容

### Week 1: LangChain 基础
**你会学到**: LLM调用、消息系统、Prompt、Chain、LCEL  
**项目**: 智能文档问答助手  
**难度**: ⭐⭐☆☆☆  
**时间**: 7天，每天2小时

### Week 2: Agent 与工具
**你会学到**: Tools、Agent、Memory、结构化输出  
**项目**: 智能客服系统  
**难度**: ⭐⭐⭐☆☆  
**时间**: 7天，每天2-3小时

### Week 3-4: LangGraph
**你会学到**: StateGraph、节点路由、Multi-Agent、中间件  
**项目**: 代码审查系统、内容生成系统  
**难度**: ⭐⭐⭐⭐☆  
**时间**: 14天，每天2-3小时

### Week 5-6: DeepAgents
**你会学到**: Agent、Task、Crew、高级模式  
**项目**: 智能代码助手（完整版）  
**难度**: ⭐⭐⭐⭐☆  
**时间**: 14天，每天2-3小时

### Week 7-8: 生产实践
**你会学到**: 性能优化、源码解读、部署运维  
**项目**: 毕业项目（自选）  
**难度**: ⭐⭐⭐⭐⭐  
**时间**: 14天，每天3-4小时

---

## ✅ 学习前检查

在开始学习前，确保：

- [ ] Python 3.11+ 已安装
- [ ] 虚拟环境已创建
- [ ] 依赖已安装（`pip install langchain langchain-anthropic python-dotenv`）
- [ ] API Key 已配置（`.env` 文件）
- [ ] 第一个示例成功运行

**检查命令**:
```bash
python --version  # 应该 >= 3.11
pip list | grep langchain  # 应该看到 langchain 和 langchain-anthropic
cat .env  # 应该看到 ANTHROPIC_API_KEY
```

---

## 🎯 学习目标设定

根据你的目标选择深度：

### 目标 1: 能用 LangChain 开发应用
**需要学习**: Week 1-2
**时间投入**: 2周
**能力**: 基础应用开发

### 目标 2: 构建复杂 AI 系统
**需要学习**: Week 1-4
**时间投入**: 4周
**能力**: 复杂工作流、Multi-Agent

### 目标 3: 成为框架专家
**需要学习**: Week 1-8（完整）
**时间投入**: 8周
**能力**: 源码级理解、生产部署、自定义扩展

---

## 📝 每日学习流程建议

### 1. 理论学习（30分钟）
- 阅读当天的README说明
- 理解核心概念
- 查看官方文档（如需要）

### 2. 代码实践（60分钟）
- 运行示例代码
- 理解每行代码的作用
- 修改参数观察变化

### 3. 完成作业（30分钟）
- 完成每日作业
- 尝试扩展功能
- 解决遇到的问题

### 4. 记录总结（10分钟）
- 记录学习笔记
- 整理遇到的问题
- 规划明天的学习

**总计**: 每天约2-2.5小时

---

## 🆘 遇到问题？

### 常见问题快速链接
- [环境配置](./docs/guides/environment_setup.md)
- [API Key配置](./docs/guides/env_config.md)
- [常见错误](./docs/guides/troubleshooting.md)
- [FAQ](./docs/guides/faq.md)

### 获取帮助
1. 查看课程文档
2. 搜索 GitHub Issues
3. 在社区提问
4. 查阅官方文档

---

## 🎉 准备好了？

### 新手从这里开始
```bash
cd week1_langchain_basics
cat README.md
python day1_hello_langchain.py
```

### 有经验的开发者从这里
```bash
cat CURRICULUM_V3.md  # 先浏览完整大纲
cd week2_agent_tools  # 或选择感兴趣的week
```

### 源码研究者从这里
```bash
cd source_code_guide
cat README.md
```

---

**记住**: 学习编程最重要的是**动手实践**。不要只看代码，一定要运行、修改、实验！

**祝你学习愉快！** 🚀💪
