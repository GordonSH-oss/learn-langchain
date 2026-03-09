# LangChain 课程更新 - 2026年3月最新版

> 基于 LangChain v1.0 和 LangGraph v1.0 的最新特性更新

## 🆕 重要更新说明

### LangChain v1.0 重大变化（2025年10月发布）

#### 1. create_agent - 新的标准API

**重大变更**：
- ✅ **新API**: `create_agent()` 取代了 `langgraph.prebuilt.create_react_agent()`
- ✅ **更简洁**: 提供更清晰、更强大的接口
- ✅ **基于LangGraph**: 底层使用 LangGraph 实现，可无缝切换到自定义工作流

**旧代码（已弃用）**：
```python
# ❌ 旧方式（LangChain < 1.0）
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(model, tools)
```

**新代码（推荐）**：
```python
# ✅ 新方式（LangChain >= 1.0）
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=tools,
    state_schema=State,  # 可选：自定义状态
    middleware=[],  # 可选：中间件
    checkpointer=checkpointer  # 可选：持久化
)
```

#### 2. 标准化内容块（Standard Content Blocks）

**新特性**：
- ✅ 统一的 `content_blocks` 属性
- ✅ 跨提供商的标准化访问
- ✅ 支持推理块、引用、工具调用等

**示例**：
```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
response = model.invoke("解释量子计算")

# 访问标准化的内容块
for block in response.content_blocks:
    if block.type == "text":
        print(block.text)
    elif block.type == "thinking":
        print(f"推理过程: {block.thinking}")
```

#### 3. 简化的命名空间

**变更**：
- ✅ `langchain` 核心包更精简
- ✅ 旧功能移至 `langchain-classic`
- ✅ 专注于 Agent 构建的核心功能

**迁移指南**：
```python
# 如果你使用旧的 Chain 或 Retriever
pip install langchain-classic

# 更新导入
from langchain import ...  # ❌
from langchain_classic import ...  # ✅

from langchain.chains import ...  # ❌
from langchain_classic.chains import ...  # ✅

from langchain.retrievers import ...  # ❌
from langchain_classic.retrievers import ...  # ✅
```

### LangGraph v1.0 核心更新

#### 1. 稳定的核心API

**特点**：
- ✅ Graph 原语（state, nodes, edges）保持不变
- ✅ 执行模型不变，升级简单
- ✅ 可靠性优先：checkpointing、persistence、streaming

#### 2. 与 LangChain v1 无缝集成

**工作流程**：
```
LangChain create_agent (高层抽象)
         ↓
    LangGraph (底层实现)
         ↓
  自定义控制 (需要时)
```

---

## 📚 更新的技术栈

### 推荐版本（2026年3月）

```bash
# Python 版本
Python 3.11+ (推荐 3.12)

# 核心框架
pip install langchain>=1.0  # LangChain v1
pip install langgraph>=1.0  # LangGraph v1
pip install langchain-core>=1.0

# LLM 提供商
pip install langchain-anthropic  # Anthropic Claude
pip install langchain-openai     # OpenAI GPT

# 额外依赖
pip install python-dotenv
pip install langgraph-checkpoint-sqlite  # 持久化支持
```

---

## 🆕 新增的最佳实践

### 1. 使用中间件（Middleware）

**新特性**：LangChain v1.0 引入了强大的中间件系统

```python
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import MemorySaver

agent = create_agent(
    model="gpt-4.1",
    tools=tools,
    middleware=[
        SummarizationMiddleware(
            model="gpt-4.1-mini",  # 使用更便宜的模型
            trigger=("tokens", 4000),  # 触发条件
            keep=("messages", 10)  # 保留最近10条消息
        )
    ],
    checkpointer=MemorySaver()
)
```

**使用场景**：
- 📝 消息历史压缩
- 🔄 自动摘要
- 🎯 上下文管理
- ⚡ 性能优化

### 2. 自定义状态Schema

**新特性**：可以扩展默认的消息状态

```python
from langchain_core.messages import MessagesState
from typing import TypedDict
from langgraph.graph import MessagesAnnotation

# 方式1：继承 MessagesState
class CustomState(MessagesState):
    user_preferences: dict[str, str]
    session_id: str

# 方式2：使用 MessagesAnnotation
from typing_extensions import TypedDict
from langgraph.graph import add_messages

class CustomState(TypedDict):
    messages: MessagesAnnotation  # 自动处理消息累加
    user_info: dict
    context: str
```

### 3. Human-in-the-Loop 模式

**更新的实现**：
```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

agent = create_agent(
    model=model,
    tools=tools,
    checkpointer=MemorySaver(),  # 必需：支持中断
)

# 配置会话ID
config = {"configurable": {"thread_id": "conversation-1"}}

# 第一次调用
result = agent.invoke({"messages": "帮我发送重要邮件"}, config)

# 如果Agent请求批准，会中断并等待
if result["interrupt"]:
    print("Agent需要批准:", result["messages"][-1].content)
    
    # 人工审核后继续
    result = agent.invoke(
        {"messages": "approved"},  # 或 "rejected"
        config
    )
```

---

## 🔄 废弃和迁移指南

### 废弃功能清单

| 功能 | 状态 | 替代方案 |
|------|------|----------|
| `create_react_agent` | ⚠️ 已弃用 | `create_agent()` |
| 旧 Chain API | ⚠️ 移至classic | 使用 Agent 或 LCEL |
| `langchain.retrievers.*` | ⚠️ 移至classic | `langchain_classic.retrievers` |
| `langchain.hub` | ⚠️ 移至classic | `langchain_classic.hub` |

### 快速迁移步骤

#### 1. 从 create_react_agent 迁移

**之前**：
```python
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
agent = create_react_agent(model, tools)

result = agent.invoke({"messages": [("user", "Hello")]})
```

**之后**：
```python
from langchain.agents import create_agent  # ✅ 新导入
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
agent = create_agent(model=model, tools=tools)  # ✅ 新API

result = agent.invoke({"messages": "Hello"})  # ✅ 简化的输入
```

#### 2. 从旧 Chain 迁移

**之前**：
```python
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Tell me about {topic}")
chain = LLMChain(llm=model, prompt=prompt)
```

**之后（方式1 - 使用 LCEL）**：
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Tell me about {topic}")
chain = prompt | model | StrOutputParser()
```

**之后（方式2 - 使用 Agent）**：
```python
from langchain.agents import create_agent

# 创建一个专门的Agent
agent = create_agent(
    model=model,
    tools=[],  # 可以添加工具
)
```

---

## 📖 更新的学习路径

### Week 1-2 更新重点

#### Day 1-2：环境和基础（更新）

**新增内容**：
```bash
# 安装最新版本
pip install langchain>=1.0 langgraph>=1.0 langchain-anthropic

# 验证版本
python -c "import langchain; print(f'LangChain {langchain.__version__}')"
python -c "import langgraph; print(f'LangGraph {langgraph.__version__}')"
```

#### Day 10-11：Agent 创建（重要更新）

**新的最佳实践**：
```python
# 文件：projects/day10_create_agent_v1.py

from langchain.agents import create_agent  # ✅ 新API
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

load_dotenv()

# 创建工具
@tool
def get_weather(city: str) -> str:
    """获取城市的天气信息"""
    return f"{city}的天气是晴天，温度25°C"

@tool
def search_web(query: str) -> str:
    """搜索网络信息"""
    return f"关于'{query}'的搜索结果..."

# 创建模型
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 使用新API创建Agent
agent = create_agent(
    model=model,
    tools=[get_weather, search_web],
    checkpointer=MemorySaver()  # 可选：持久化
)

# 运行Agent
config = {"configurable": {"thread_id": "test-1"}}
result = agent.invoke(
    {"messages": "北京的天气怎么样？"},
    config
)

print(result["messages"][-1].content)
```

### Week 3-4 更新重点

#### LangGraph 核心（保持稳定）

**核心API未变**：
- ✅ `StateGraph` - 状态图定义
- ✅ `add_node` - 添加节点
- ✅ `add_edge` - 添加边
- ✅ `compile` - 编译图

**新增特性**：
```python
from langgraph.graph import StateGraph, START, END, MessagesAnnotation
from typing_extensions import TypedDict

class State(TypedDict):
    messages: MessagesAnnotation  # ✅ 新：自动消息处理
    custom_data: str

graph = StateGraph(State)
graph.add_node("node1", node1_func)
graph.add_node("node2", node2_func)
graph.add_edge(START, "node1")
graph.add_edge("node1", "node2")
graph.add_edge("node2", END)

app = graph.compile()
```

---

## 🆕 新增教程主题

### 1. Middleware 深入

**主题**：使用中间件增强Agent功能

**内容**：
- 消息摘要中间件
- 自定义中间件开发
- 中间件组合

### 2. 多模态 Agent

**更新**：支持图像、音频、视频输入

**示例**：
```python
from langchain_core.messages import HumanMessage

# 发送图像
message = HumanMessage(
    content=[
        {"type": "text", "text": "这张图片里有什么？"},
        {
            "type": "image_url",
            "image_url": {"url": "https://example.com/image.jpg"}
        }
    ]
)

result = agent.invoke({"messages": [message]})
```

### 3. LangSmith 集成

**新增**：生产环境监控和调试

**快速开始**：
```python
import os
os.environ["LANGSMITH_API_KEY"] = "your-api-key"
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "my-project"

# Agent自动追踪到LangSmith
agent = create_agent(model=model, tools=tools)
```

---

## 📝 更新的代码示例

### 示例1：现代化的RAG Agent

```python
# 文件：projects/modern_rag_agent.py

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

load_dotenv()

# 1. 加载和索引文档
loader = WebBaseLoader("https://docs.langchain.com/")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(docs)

vectorstore = FAISS.from_documents(
    splits,
    OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
)
retriever = vectorstore.as_retriever()

# 2. 创建检索工具
@tool
def search_docs(query: str) -> str:
    """在LangChain文档中搜索信息"""
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])

# 3. 创建RAG Agent
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

agent = create_agent(
    model=model,
    tools=[search_docs],
    checkpointer=MemorySaver()
)

# 4. 使用Agent
config = {"configurable": {"thread_id": "rag-session"}}

questions = [
    "什么是LangChain？",
    "如何创建Agent？",
    "LangGraph的主要特性是什么？"
]

for q in questions:
    result = agent.invoke({"messages": q}, config)
    print(f"\nQ: {q}")
    print(f"A: {result['messages'][-1].content}\n")
```

### 示例2：带中间件的Agent

```python
# 文件：projects/agent_with_middleware.py

from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创建带中间件的Agent
agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        SummarizationMiddleware(
            model="gpt-4.1-mini",  # 使用更便宜的模型做摘要
            trigger=("tokens", 4000),  # 超过4000 tokens时触发
            keep=("messages", 10)  # 保留最近10条消息
        )
    ],
    checkpointer=MemorySaver()
)

# 模拟长对话
config = {"configurable": {"thread_id": "long-conversation"}}

for i in range(20):
    result = agent.invoke(
        {"messages": f"这是第{i+1}条消息，请简短回复"},
        config
    )
    print(f"Round {i+1}: {result['messages'][-1].content[:100]}...")
```

---

## 🎯 更新的实战项目

### 项目更新：Week 1 智能文档助手

**使用最新API重写**：
```python
# 使用 create_agent 替代旧的实现
# 添加 middleware 支持
# 集成 LangSmith 追踪
```

### 新项目：多模态内容分析器

**功能**：
- 分析图片内容
- 提取视频关键帧
- 音频转文字
- 跨模态问答

---

## 📊 性能和成本优化

### 1. 使用不同模型

```python
# 主任务使用强大模型
main_model = "claude-3-5-sonnet-20241022"

# 摘要使用便宜模型
summary_model = "gpt-4.1-mini"

# 工具调用使用中等模型
tool_model = "claude-haiku-4-5-20251001"
```

### 2. 缓存策略

```python
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache

set_llm_cache(InMemoryCache())
```

### 3. 流式输出

```python
# 使用 stream 替代 invoke
for chunk in agent.stream({"messages": "长文本生成任务"}, config):
    if "messages" in chunk:
        print(chunk["messages"][-1].content, end="", flush=True)
```

---

## 🔗 官方资源链接

### 文档
- [LangChain v1 发布说明](https://docs.langchain.com/oss/python/releases/langchain-v1)
- [LangGraph v1 发布说明](https://docs.langchain.com/oss/python/releases/langgraph-v1)
- [迁移指南](https://docs.langchain.com/oss/python/releases/langchain-v1#migration-guide)
- [create_agent API文档](https://docs.langchain.com/oss/python/langchain/agents)

### 示例
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangGraph 示例](https://github.com/langchain-ai/langgraph/tree/main/examples)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain/tree/master/cookbook)

---

## ✅ 更新检查清单

在学习新课程前，请确认：

- [ ] Python 版本 >= 3.11
- [ ] 安装 LangChain >= 1.0
- [ ] 安装 LangGraph >= 1.0
- [ ] 了解 `create_agent` 新API
- [ ] 知道旧代码的迁移路径
- [ ] 配置好 API Keys
- [ ] （可选）注册 LangSmith 账号

---

**更新日期**：2026年3月4日  
**适用课程**：`CURRICULUM_MASTER.md` 和 `CURRICULUM_WEEK2-8.md`  
**下一次更新**：定期跟踪官方发布，每季度更新一次
