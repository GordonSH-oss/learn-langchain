# LangChain/LangGraph/DeepAgents 源码学习指南

> 深入理解框架原理，掌握核心实现

## 📖 为什么要学习源码？

学习源码能帮助你：
1. **深入理解框架设计**：了解架构决策和设计模式
2. **解决问题更快**：遇到bug能快速定位原因
3. **贡献开源**：能够参与框架开发和改进
4. **提升编程能力**：学习优秀的代码组织方式
5. **自定义扩展**：能够创建自己的组件和插件

## 🎯 学习建议

### 1. 循序渐进
- 先掌握使用，再学习源码
- 从核心概念入手，逐步深入
- 不要一开始就想理解所有细节

### 2. 带着问题学习
- "create_agent是如何工作的？"
- "State是如何更新的？"
- "Tool调用的完整流程是什么？"

### 3. 动手实践
- 阅读源码时，尝试修改代码
- 实现自定义组件
- 编写测试用例验证理解

### 4. 做好笔记
- 绘制架构图
- 记录关键代码片段
- 整理设计模式和技巧

## 📚 学习路径

### Week 7-8 学习安排

```
Week 7: LangChain & LangGraph 源码
├── Day 48-49: LangChain核心
│   ├── 架构设计
│   ├── Runnable接口
│   ├── Chain实现
│   └── Agent实现
│
└── Day 50-51: LangGraph实现
    ├── 架构设计
    ├── StateGraph实现
    ├── 状态管理
    └── Checkpointer系统

Week 8: DeepAgents 源码
└── Day 52-53: DeepAgents架构
    ├── Agent执行引擎
    ├── Task调度器
    ├── Crew管理器
    └── Process实现
```

## 🔍 源码导读目录

### 1. LangChain源码导读

📁 **[langchain/](./langchain/)**

- [01_architecture.md](./langchain/01_architecture.md) - LangChain架构概览
- [02_runnable.md](./langchain/02_runnable.md) - Runnable接口设计
- [03_chains.md](./langchain/03_chains.md) - Chain实现原理
- [04_agents.md](./langchain/04_agents.md) - Agent实现细节
- [annotated_code/](./langchain/annotated_code/) - 带注释的核心源码

**核心主题：**
- Runnable协议和LCEL实现
- Chain的组合和执行
- Agent的工作流程
- 工具调用机制

---

### 2. LangGraph源码导读

📁 **[langgraph/](./langgraph/)**

- [01_architecture.md](./langgraph/01_architecture.md) - LangGraph架构设计
- [02_graph.md](./langgraph/02_graph.md) - StateGraph实现
- [03_state.md](./langgraph/03_state.md) - 状态管理机制
- [04_checkpointer.md](./langgraph/04_checkpointer.md) - Checkpointer系统
- [annotated_code/](./langgraph/annotated_code/) - 带注释的核心源码

**核心主题：**
- StateGraph的构建和执行
- 状态更新和传递
- 条件路由实现
- Checkpointer持久化

---

### 3. DeepAgents源码导读

📁 **[deepagents/](./deepagents/)**

- [01_architecture.md](./deepagents/01_architecture.md) - DeepAgents架构
- [02_agent.md](./deepagents/02_agent.md) - Agent实现
- [03_task.md](./deepagents/03_task.md) - Task系统
- [04_crew.md](./deepagents/04_crew.md) - Crew管理
- [annotated_code/](./deepagents/annotated_code/) - 带注释的核心源码

**核心主题：**
- Agent角色定义和执行
- Task依赖和调度
- Crew的Process模式
- 多Agent协作机制

---

## 🛠️ 源码阅读工具

### 1. IDE设置
- **VSCode**: 安装Python插件，启用类型检查
- **PyCharm**: 使用专业版的代码导航功能

### 2. 调试技巧
```python
# 在源码中添加断点
import pdb; pdb.set_trace()

# 打印调用栈
import traceback
traceback.print_stack()

# 查看对象属性
print(dir(obj))
print(vars(obj))
```

### 3. 代码导航
- "跳转到定义" (Ctrl/Cmd + Click)
- "查找引用" (Shift + F12)
- "查看类层次结构"

## 📝 学习任务

### Task 1: 追踪一个完整调用
选择一个简单的示例，追踪完整的执行流程：
```python
# 示例：追踪 model.invoke() 的执行
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
response = model.invoke([HumanMessage(content="Hi")])

# 追踪问题：
# 1. invoke方法是如何实现的？
# 2. 消息是如何序列化的？
# 3. API调用是在哪里发生的？
# 4. 响应是如何解析的？
```

### Task 2: 实现自定义组件
基于源码理解，实现自己的组件：
```python
from langchain_core.runnables import Runnable

class MyCustomRunnable(Runnable):
    """自定义Runnable组件"""
    
    def invoke(self, input, config=None):
        # TODO: 实现你的逻辑
        pass
```

### Task 3: 绘制架构图
为每个框架绘制架构图：
- 核心类和接口
- 主要的数据流
- 关键的交互点

## 💡 源码阅读技巧

### 1. 从接口开始
先看公共API和抽象基类，理解设计意图。

### 2. 关注测试用例
测试用例展示了组件的使用方式和边界情况。

### 3. 使用示例验证
运行官方示例，在关键点添加打印语句。

### 4. 对比不同版本
查看Git历史，了解设计演变。

## 📖 推荐阅读顺序

### 第1阶段：接口和抽象（Day 48）
1. Runnable接口
2. 基础抽象类
3. 类型定义

### 第2阶段：核心实现（Day 49）
1. Chain实现
2. Agent实现  
3. Tool调用

### 第3阶段：LangGraph（Day 50-51）
1. StateGraph构建
2. 节点执行
3. 状态管理
4. Checkpointer

### 第4阶段：DeepAgents（Day 52-53）
1. Agent引擎
2. Task调度
3. Crew管理
4. Process模式

## 🎓 学习成果

完成源码学习后，你应该能够：
- [ ] 理解框架的整体架构
- [ ] 解释核心概念的实现原理
- [ ] 创建自定义组件和扩展
- [ ] 调试和解决框架相关问题
- [ ] 参与开源贡献

## 🔗 官方资源

### LangChain
- GitHub: https://github.com/langchain-ai/langchain
- 开发者文档: https://python.langchain.com/docs/contributing/

### LangGraph
- GitHub: https://github.com/langchain-ai/langgraph
- 开发者文档: https://langchain-ai.github.io/langgraph/

### DeepAgents
- GitHub: https://github.com/deepagents/deepagents

## 📢 获取帮助

- 阅读源码时遇到问题？在社区提问
- 发现代码问题？提交GitHub Issue
- 有改进想法？提交Pull Request

---

**准备好深入源码了吗？从 [LangChain架构概览](./langchain/01_architecture.md) 开始！** 🚀
