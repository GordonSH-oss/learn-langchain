# Agent State 字段说明：固定字段 vs 自定义字段

## 📋 核心概念

在 LangChain/LangGraph 的 Agent 中，`invoke()` 方法接收的字段分为两类：

1. **固定字段**：`AgentState` 基类中定义的标准字段（如 `messages`）
2. **自定义字段**：通过继承 `AgentState` 添加的自定义字段（如 `user_id`, `user_name` 等）

## 🔍 代码分析

### 1. 固定字段（AgentState 标准字段）

`AgentState` 是 LangChain 提供的基类，包含以下**固定字段**：

```python
from langchain.agents import AgentState

# AgentState 的标准字段包括：
# - messages: List[BaseMessage]  # 消息历史（必需）
# - next: List[str]  # 下一步要执行的节点（可选）
# - ... 其他标准字段
```

**最重要的固定字段：**
- ✅ `messages`: 消息列表，**这是必需的字段**
- ✅ `next`: 下一步节点（通常由 Agent 自动管理）

### 2. 自定义字段（通过继承添加）

在你的代码中，通过继承 `AgentState` 添加了自定义字段：

```python
class CustomAgentState(AgentState):
    """扩展 AgentState 添加自定义字段"""
    user_id: str          # 👈 自定义字段
    user_name: str        # 👈 自定义字段
    preferences: dict     # 👈 自定义字段
    interaction_count: int # 👈 自定义字段
```

### 3. 使用自定义 State

创建 Agent 时指定使用自定义 State：

```python
agent = create_agent(
    model=model,
    tools=[...],
    state_schema=CustomAgentState,  # 👈 指定使用自定义 State
    checkpointer=InMemorySaver(),
)
```

### 4. 在 invoke 中传入字段

```python
result = agent.invoke(
    {
        # ✅ 固定字段（必需）
        "messages": [{"role": "user", "content": "..."}],
        
        # ✅ 自定义字段（可选，但必须在 CustomAgentState 中定义）
        "user_id": "user_123",
        "user_name": "Alice",
        "preferences": {"theme": "dark"},
        "interaction_count": 1,
    },
    config={"configurable": {"thread_id": thread_id}}
)
```

## 📊 字段分类总结

| 字段名 | 类型 | 说明 |
|--------|------|------|
| `messages` | **固定** | AgentState 标准字段，必需 |
| `next` | **固定** | AgentState 标准字段，通常自动管理 |
| `user_id` | **自定义** | 在 CustomAgentState 中定义 |
| `user_name` | **自定义** | 在 CustomAgentState 中定义 |
| `preferences` | **自定义** | 在 CustomAgentState 中定义 |
| `interaction_count` | **自定义** | 在 CustomAgentState 中定义 |

## 🎯 如何判断字段是固定还是自定义？

### 方法1: 查看 State 类定义

```python
# 查看 AgentState 的源码或文档
from langchain.agents import AgentState
import inspect

# 查看 AgentState 的所有字段
print(inspect.signature(AgentState))
```

### 方法2: 查看你的自定义 State 类

```python
class CustomAgentState(AgentState):
    # 这些是自定义字段
    user_id: str
    user_name: str
    preferences: dict
    interaction_count: int
```

### 方法3: 查看 create_agent 的 state_schema 参数

```python
agent = create_agent(
    state_schema=CustomAgentState,  # 👈 这里指定的类定义了所有可用字段
    ...
)
```

## 💡 实际示例对比

### 示例1: 只使用固定字段（最简单）

```python
from langchain.agents import create_agent, AgentState

# 使用默认的 AgentState（只有固定字段）
agent = create_agent(model=model, tools=[...])

# invoke 时只能传入固定字段
result = agent.invoke({
    "messages": [{"role": "user", "content": "Hello"}]
    # ❌ 不能传入 user_id, user_name 等自定义字段
})
```

### 示例2: 使用自定义字段（你的代码）

```python
class CustomAgentState(AgentState):
    user_id: str
    user_name: str
    preferences: dict
    interaction_count: int

# 使用自定义 State
agent = create_agent(
    model=model,
    tools=[...],
    state_schema=CustomAgentState,  # 👈 指定自定义 State
)

# invoke 时可以传入固定字段 + 自定义字段
result = agent.invoke({
    "messages": [{"role": "user", "content": "Hello"}],  # ✅ 固定字段
    "user_id": "user_123",                                # ✅ 自定义字段
    "user_name": "Alice",                                 # ✅ 自定义字段
    "preferences": {"theme": "dark"},                     # ✅ 自定义字段
    "interaction_count": 1,                               # ✅ 自定义字段
})
```

## ⚠️ 注意事项

### 1. 字段类型必须匹配

```python
class CustomAgentState(AgentState):
    user_id: str  # 定义为 str

# ✅ 正确
agent.invoke({"messages": [...], "user_id": "user_123"})

# ❌ 错误：类型不匹配
agent.invoke({"messages": [...], "user_id": 123})  # 应该是字符串
```

### 2. 必需字段必须提供

```python
# ❌ 错误：缺少必需的 messages 字段
agent.invoke({"user_id": "user_123"})

# ✅ 正确：包含必需的 messages
agent.invoke({
    "messages": [...],  # 必需
    "user_id": "user_123"  # 可选（如果在 State 中定义了）
})
```

### 3. 未定义的字段会被忽略

```python
class CustomAgentState(AgentState):
    user_id: str
    # 没有定义 user_email

# ⚠️ 传入未定义的字段会被忽略（不会报错，但也不会被使用）
agent.invoke({
    "messages": [...],
    "user_id": "user_123",      # ✅ 会被使用
    "user_email": "alice@example.com"  # ⚠️ 会被忽略
})
```

## 🔧 如何添加更多自定义字段？

### 步骤1: 扩展 CustomAgentState

```python
class CustomAgentState(AgentState):
    # 原有字段
    user_id: str
    user_name: str
    preferences: dict
    interaction_count: int
    
    # 新增字段
    session_id: str           # 👈 新增
    last_active_time: float   # 👈 新增
    metadata: dict           # 👈 新增
```

### 步骤2: 在 invoke 中使用新字段

```python
result = agent.invoke({
    "messages": [...],
    "user_id": "user_123",
    "session_id": "session_001",      # 👈 使用新字段
    "last_active_time": 1234567890.0, # 👈 使用新字段
    "metadata": {"source": "web"},    # 👈 使用新字段
})
```

## 📚 相关资源

- [LangGraph State 文档](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)
- [LangChain AgentState 源码](https://github.com/langchain-ai/langchain/blob/main/libs/langchain/langchain/agents/__init__.py)
- [TypedDict 类型注解](https://docs.python.org/3/library/typing.html#typing.TypedDict)

## 🎓 总结

**回答你的问题：**

> invoke 可以带的这些字段，是自定义的，还是固定的？

**答案：混合的！**

- ✅ `messages` - **固定字段**（AgentState 标准字段，必需）
- ✅ `user_id`, `user_name`, `preferences`, `interaction_count` - **自定义字段**（在 `CustomAgentState` 中定义）

**判断方法：**
1. 查看 `state_schema` 参数指定的类（你的代码中是 `CustomAgentState`）
2. 该类继承自 `AgentState`，所以包含所有固定字段
3. 该类中额外定义的字段就是自定义字段
4. `invoke()` 可以传入：固定字段 + 自定义字段

