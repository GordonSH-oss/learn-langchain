# LangChain & LangGraph 30天学习计划

> 系统化学习LangChain和LangGraph，从入门到精通

## 📅 学习概览

- **总时长**: 30天
- **每天投入**: 2-3小时
- **学习方式**: 理论学习 + 实践编码
- **项目结构**: 每周一个主题，周末实战项目

---

## 第一周：LangChain基础（Day 1-7）

### Day 1：环境搭建和基础概念

**学习目标**：
- 了解LangChain和LangGraph的基本概念
- 配置开发环境
- 运行第一个LLM应用

**学习内容**：
1. 阅读项目README和环境配置指南
2. 安装依赖和配置API Keys
3. 理解LLM、Prompt、Message的概念

**实践任务**：
```bash
# 1. 安装依赖
pip install langchain langchain-anthropic python-dotenv

# 2. 配置.env文件
cp .env.example .env
# 编辑.env，填入API Key

# 3. 运行第一个示例
python examples/use-agent-anthropic-qa-only.py
```

**参考文档**：
- [环境配置指南](docs/guides/ENV_CONFIG_GUIDE.md)
- [Anthropic Agent指南](ANTHROPIC_AGENT_README.md)

---

### Day 2：理解消息和对话

**学习目标**：
- 掌握不同类型的消息（HumanMessage, AIMessage, SystemMessage）
- 理解对话上下文的管理
- 实现多轮对话

**学习内容**：
1. 消息类型和格式
2. System Prompt的作用
3. 对话历史的维护

**实践任务**：
```python
# 创建一个支持多轮对话的程序
# 文件：my_first_chat.py

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 实现一个命令行对话程序
messages = [
    SystemMessage(content="你是一个友好的AI助手，擅长回答编程问题。")
]

while True:
    user_input = input("你: ")
    if user_input.lower() in ['quit', 'exit', '退出']:
        break
    
    messages.append(HumanMessage(content=user_input))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    
    print(f"AI: {response.content}\n")
```

**参考资料**：
- `examples/use-agent-anthropic-qa-only.py`

---

### Day 3：Prompt工程

**学习目标**：
- 学习如何编写有效的Prompt
- 理解Few-shot Learning
- 掌握Prompt模板的使用

**学习内容**：
1. Prompt设计原则
2. Few-shot示例
3. ChatPromptTemplate的使用

**实践任务**：
编写不同场景的Prompt：
- 代码生成
- 文本摘要
- 问答助手
- 翻译工具

**参考代码**：
```python
from langchain_core.prompts import ChatPromptTemplate

# 创建代码生成Prompt
code_gen_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个Python专家，擅长编写清晰、高效的代码。"),
    ("human", "请帮我写一个函数：{requirement}"),
])

# 使用
messages = code_gen_prompt.format_messages(
    requirement="读取JSON文件并解析内容"
)
```

---

### Day 4-5：工具（Tools）基础

**学习目标**：
- 理解工具的概念和作用
- 学会创建自定义工具
- 了解工具调用的流程

**学习内容**：
1. 什么是Tool
2. 使用@tool装饰器
3. 工具的参数和返回值
4. 工具的描述（用于LLM理解）

**实践任务**：

**Day 4 - 创建基础工具**：
```python
# 文件：my_tools.py

from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """执行数学计算。输入应该是一个数学表达式，例如: '2+2' 或 '10*5'"""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

@tool
def get_current_time() -> str:
    """获取当前时间"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def search_wikipedia(query: str) -> str:
    """搜索维基百科（模拟）"""
    return f"这是关于'{query}'的模拟搜索结果..."
```

**Day 5 - 测试工具**：
```bash
python examples/use-agent-tool.py
```

**参考文档**：
- `examples/use-agent-tool.py`

---

### Day 6-7：周末实战项目1 - 智能计算器

**项目目标**：
创建一个智能计算器Agent，能够：
- 理解自然语言数学问题
- 调用计算器工具
- 返回格式化的结果

**功能需求**：
1. 支持基础数学运算
2. 支持复杂表达式
3. 友好的错误提示
4. 对话式交互

**实现步骤**：
```python
# 文件：projects/calculator_agent.py

from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
from langchain.agents import create_agent
import os
from dotenv import load_dotenv

load_dotenv()

# 1. 创建工具
@tool
def calculator(expression: str) -> str:
    """执行数学计算"""
    # 实现计算逻辑
    pass

# 2. 创建Agent
model = ChatAnthropic(...)
agent = create_agent(
    model=model,
    tools=[calculator],
    system_prompt="你是一个数学助手..."
)

# 3. 实现交互界面
def main():
    print("智能计算器启动！")
    while True:
        question = input("请输入计算问题（输入'退出'结束）: ")
        if question == "退出":
            break
        # 调用agent并显示结果
        result = agent.invoke({"messages": [...]})
        print(f"结果: {result}\n")

if __name__ == "__main__":
    main()
```

**提交要求**：
- 代码能够正常运行
- 包含至少5个测试用例
- 添加README说明使用方法

---

## 第二周：Agent进阶（Day 8-14）

### Day 8-9：Agent概念和创建

**学习目标**：
- 理解Agent的工作原理
- 学会使用create_agent
- 掌握Agent的配置参数

**学习内容**：
1. Agent vs 简单LLM调用
2. ReAct模式
3. create_agent函数的参数
4. Agent的执行流程

**实践任务**：
```bash
# 研究示例代码
python examples/use-agent-anthropic-simple.py

# 阅读源码分析
```

**参考文档**：
- `examples/use-agent-anthropic-simple.py`
- [create_agent源码分析](docs/advanced/create-agent-analysis.md)

---

### Day 10-11：真实API集成

**学习目标**：
- 学会集成外部API
- 处理HTTP请求和响应
- 实现错误处理

**学习内容**：
1. 使用requests库
2. API认证
3. 数据解析
4. 错误处理和重试

**实践任务**：

**Day 10 - 学习天气API**：
1. 注册OpenWeatherMap账号
2. 获取API Key
3. 阅读文档并测试API

**Day 11 - 实现天气Agent**：
```bash
# 运行天气示例
python examples/use-agent-tool-real-weather.py
```

**参考文档**：
- [天气API指南](docs/guides/WEATHER_API_GUIDE.md)
- `examples/use-agent-tool-real-weather.py`

---

### Day 12：输出解析和结构化输出

**学习目标**：
- 理解为什么需要结构化输出
- 学会使用Pydantic模型
- 掌握输出解析器

**学习内容**：
1. Pydantic BaseModel
2. ToolStrategy vs ProviderStrategy
3. 自定义Schema

**实践任务**：
```python
# 创建结构化输出示例
from pydantic import BaseModel, Field
from langchain.agents import create_agent, ToolStrategy

class WeatherInfo(BaseModel):
    """天气信息"""
    location: str = Field(description="城市名称")
    temperature: float = Field(description="温度（摄氏度）")
    condition: str = Field(description="天气状况")
    humidity: int = Field(description="湿度百分比")

# 使用结构化输出
agent = create_agent(
    model=model,
    tools=[get_weather],
    response_format=ToolStrategy(schema=WeatherInfo)
)
```

**参考文档**：
- [ToolStrategy原理](docs/advanced/tool-strategy-analysis.md)

---

### Day 13-14：周末实战项目2 - 新闻摘要助手

**项目目标**：
创建一个新闻摘要Agent：
- 从API获取新闻
- 生成结构化摘要
- 支持多个新闻源

**功能需求**：
1. 集成新闻API（如NewsAPI）
2. 返回结构化数据
3. 生成摘要和关键词
4. 支持类别筛选

**数据结构**：
```python
from pydantic import BaseModel
from typing import List

class NewsSummary(BaseModel):
    title: str
    summary: str
    keywords: List[str]
    category: str
    url: str
```

---

## 第三周：LangGraph核心（Day 15-21）

### Day 15-16：StateGraph基础

**学习目标**：
- 理解状态图的概念
- 学会创建StateGraph
- 掌握节点和边的定义

**学习内容**：
1. 什么是StateGraph
2. MessagesState
3. 节点（Node）的概念
4. 边（Edge）的类型

**实践任务**：
```python
# 创建第一个StateGraph
from langgraph.graph import StateGraph, MessagesState

# 定义节点
def my_node(state: MessagesState):
    # 处理逻辑
    return {"messages": [...]}

# 创建图
workflow = StateGraph(MessagesState)
workflow.add_node("node1", my_node)
workflow.set_entry_point("node1")
workflow.add_edge("node1", "__end__")

app = workflow.compile()
```

**参考代码**：
- `examples/use-agent-anthropic-langgraph.py`

---

### Day 17-18：条件路由和分支

**学习目标**：
- 理解条件边
- 实现路由逻辑
- 掌握循环结构

**学习内容**：
1. add_conditional_edges
2. 路由函数的编写
3. 多分支决策
4. 循环处理

**实践任务**：
```python
# 实现条件路由
def router(state: MessagesState) -> str:
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"

workflow.add_conditional_edges(
    "agent",
    router,
    {
        "tools": "tools",
        "end": "__end__"
    }
)
```

---

### Day 19：自定义State Schema

**学习目标**：
- 理解AgentState的结构
- 学会自定义State字段
- 掌握状态更新机制

**学习内容**：
1. AgentState的核心字段
2. 添加自定义字段
3. 状态的reducer函数
4. 状态的更新和合并

**实践任务**：
```python
from langchain.agents import AgentState
from typing import Annotated
from langgraph.graph import add_messages

class CustomAgentState(AgentState):
    """自定义State"""
    user_id: str
    user_name: str
    session_count: int
    preferences: dict
```

**参考文档**：
- [AgentState详解](docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md)
- `examples/compare-state-fields.py`

---

### Day 20-21：周末实战项目3 - 多步骤任务Agent

**项目目标**：
创建一个能够处理多步骤任务的Agent：
- 任务规划
- 步骤执行
- 结果汇总

**应用场景**：
"帮我调研一下Python Web框架，比较Django和Flask的优缺点，并给出选择建议"

**实现步骤**：
1. 任务分解节点：将复杂任务分解为子任务
2. 执行节点：执行每个子任务
3. 汇总节点：整合所有结果
4. 路由逻辑：决定下一步执行哪个节点

---

## 第四周：生产实践（Day 22-30）

### Day 22-23：记忆和持久化

**学习目标**：
- 理解Checkpointer机制
- 实现会话持久化
- 管理多用户状态

**学习内容**：
1. MemorySaver vs InMemorySaver
2. 线程ID（thread_id）的使用
3. 状态的保存和恢复
4. 用户信息的管理

**实践任务**：
```bash
# 学习记忆管理
python examples/use-agent-with-memory-1.py
python examples/use-agent-with-memory-improved.py
python examples/use-agent-with-memory-realistic.py  # 重点
```

**参考文档**：
- [用户信息管理](docs/guides/HOW_TO_FILL_USER_INFO.md)（⭐ 重要）

---

### Day 24-25：错误处理和监控

**学习目标**：
- 实现完善的错误处理
- 添加日志和监控
- 处理API限流

**学习内容**：
1. 异常处理策略
2. 重试机制
3. 日志记录
4. 性能监控

**实践任务**：
```python
# 实现健壮的Agent
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def call_llm_with_retry(model, messages):
    try:
        response = model.invoke(messages)
        logger.info(f"LLM调用成功，tokens: {response.usage_metadata}")
        return response
    except Exception as e:
        logger.error(f"LLM调用失败: {e}")
        raise
```

---

### Day 26-28：综合项目 - 智能客服系统

**项目描述**：
构建一个完整的智能客服系统，具备以下功能：

**核心功能**：
1. **用户认证和会话管理**
   - 用户信息从数据库获取
   - 会话持久化
   - 多轮对话支持

2. **意图识别和路由**
   - 识别用户意图（咨询、投诉、查询等）
   - 路由到不同的处理流程

3. **知识库查询**
   - 集成FAQ
   - 文档检索
   - 相似问题匹配

4. **工具调用**
   - 订单查询
   - 退款处理
   - 物流追踪

5. **人工转接**
   - 判断何时需要人工
   - 记录转接原因
   - 上下文传递

**技术架构**：
```
用户输入
  ↓
意图识别节点 → [咨询] → 知识库查询 → 回复
  ↓            [投诉] → 问题记录 → 道歉回复
  ↓            [查询] → 工具调用 → 结果展示
  ↓            [复杂] → 人工转接
条件路由
```

**Day 26 - 系统设计和基础框架**：
- 设计State Schema
- 创建StateGraph结构
- 实现基础节点

**Day 27 - 功能实现**：
- 实现所有工具
- 添加条件路由
- 集成知识库

**Day 28 - 测试和优化**：
- 编写测试用例
- 性能优化
- 错误处理

**项目结构**：
```
projects/customer_service/
├── README.md
├── main.py                 # 主程序
├── agent.py                # Agent定义
├── tools/                  # 工具集
│   ├── __init__.py
│   ├── order.py           # 订单查询
│   ├── refund.py          # 退款处理
│   └── logistics.py       # 物流追踪
├── knowledge/             # 知识库
│   └── faq.json
├── models/                # 数据模型
│   └── state.py
└── tests/                 # 测试
    └── test_agent.py
```

---

### Day 29：性能优化和最佳实践

**学习目标**：
- 优化Agent性能
- 降低API成本
- 提升用户体验

**优化方向**：
1. **缓存策略**
   - 缓存常见问题的回答
   - 缓存工具调用结果

2. **Prompt优化**
   - 减少不必要的token
   - 使用更小的模型处理简单任务

3. **异步处理**
   - 使用异步API调用
   - 并行处理独立任务

4. **监控和分析**
   - Token使用统计
   - 响应时间分析
   - 成功率监控

**实践任务**：
对Day 26-28的项目进行优化

---

### Day 30：总结和进阶方向

**学习目标**：
- 回顾30天学习内容
- 规划进阶学习路径
- 探索高级话题

**总结内容**：
1. **知识回顾**
   - LangChain核心概念
   - Agent的工作原理
   - LangGraph状态管理
   - 生产环境最佳实践

2. **项目展示**
   - 整理所有练习代码
   - 完善项目文档
   - 准备作品集

3. **进阶方向**
   - RAG（检索增强生成）
   - Multi-Agent系统
   - 长期记忆管理
   - 自定义LLM集成
   - 向量数据库
   - Streaming输出
   - 函数调用优化

**下一步学习资源**：
- LangChain官方高级教程
- LangGraph cookbook
- 开源项目学习：
  - LangChain-Chatchat
  - AutoGPT
  - BabyAGI

---

## 📊 学习评估

### 第一周测试
- [ ] 能独立配置开发环境
- [ ] 理解消息类型和对话管理
- [ ] 能创建简单的工具
- [ ] 完成智能计算器项目

### 第二周测试
- [ ] 理解Agent的工作原理
- [ ] 能集成外部API
- [ ] 掌握结构化输出
- [ ] 完成新闻摘要助手

### 第三周测试
- [ ] 能创建StateGraph
- [ ] 理解条件路由
- [ ] 会自定义State Schema
- [ ] 完成多步骤任务Agent

### 第四周测试
- [ ] 实现会话持久化
- [ ] 完善错误处理
- [ ] 完成智能客服系统
- [ ] 能够优化Agent性能

---

## 💡 学习建议

### 1. 每日学习流程
```
理论学习（30分钟）
   ↓
阅读文档和示例代码（30分钟）
   ↓
动手实践（60分钟）
   ↓
总结笔记（30分钟）
```

### 2. 实践原则
- **不要只看代码**：一定要自己动手写
- **不要跳步**：按顺序学习，打好基础
- **多做实验**：尝试修改参数，观察效果
- **记录问题**：遇到问题及时记录和解决

### 3. 学习资源使用
- 官方文档是最权威的资料
- 项目中的示例代码都可以直接运行
- 进阶文档包含深入的原理解析
- 善用GPT/Claude辅助学习

### 4. 时间安排建议
- **工作日**：每天2小时（晚上）
- **周末**：每天4-5小时（上午+下午）
- **项目周**：适当增加时间投入

---

## 🎯 学习成果

完成30天学习后，你将能够：

✅ 熟练使用LangChain和LangGraph开发AI应用  
✅ 创建复杂的Multi-step Agent  
✅ 集成各种外部API和工具  
✅ 实现生产级的会话管理  
✅ 处理错误和优化性能  
✅ 独立完成完整的AI项目  

---

## 📞 学习支持

遇到问题时：
1. 查看项目文档和示例代码
2. 搜索官方文档
3. 在社区提问
4. 查看GitHub Issues

**记住**：学习编程最重要的是**动手实践**！每天坚持写代码，30天后你会看到质的飞跃。

祝学习愉快！🚀
