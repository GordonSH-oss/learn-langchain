"""
对比示例：固定字段 vs 自定义字段

这个示例展示了：
1. 只使用固定字段的 Agent
2. 使用自定义字段的 Agent
3. 如何判断字段是固定还是自定义
"""

import os
from dotenv import load_dotenv
from langchain.agents import create_agent, AgentState
from langchain_openai import ChatOpenAI
from langchain.tools import tool

load_dotenv()

# ==================== 示例1: 只使用固定字段 ====================
print("=" * 60)
print("示例1: 只使用固定字段（默认 AgentState）")
print("=" * 60)

@tool
def simple_tool(query: str) -> str:
    """简单的工具"""
    return f"处理查询: {query}"

model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# 使用默认的 AgentState（只有固定字段）
agent_default = create_agent(
    model=model,
    tools=[simple_tool],
)

# ✅ 只能传入固定字段
try:
    result1 = agent_default.invoke({
        "messages": [{"role": "user", "content": "Hello"}]
        # 注意：这里不能传入 user_id, user_name 等自定义字段
        # 因为默认的 AgentState 没有定义这些字段
    })
    print("✅ 成功：使用固定字段 messages")
    print(f"响应: {result1['messages'][-1].content[:50]}...")
except Exception as e:
    print(f"❌ 错误: {e}")

print()

# ==================== 示例2: 使用自定义字段 ====================
print("=" * 60)
print("示例2: 使用自定义字段（扩展 AgentState）")
print("=" * 60)

# 定义自定义 State
class CustomAgentState(AgentState):
    """扩展 AgentState 添加自定义字段"""
    # 👇 这些是自定义字段
    user_id: str
    user_name: str
    preferences: dict
    interaction_count: int

# 使用自定义 State
agent_custom = create_agent(
    model=model,
    tools=[simple_tool],
    state_schema=CustomAgentState,  # 👈 指定使用自定义 State
)

# ✅ 可以传入固定字段 + 自定义字段
try:
    result2 = agent_custom.invoke({
        # 固定字段（必需）
        "messages": [{"role": "user", "content": "Hello"}],
        
        # 自定义字段（可选，但必须在 CustomAgentState 中定义）
        "user_id": "user_123",
        "user_name": "Alice",
        "preferences": {"theme": "dark"},
        "interaction_count": 1,
    })
    print("✅ 成功：使用固定字段 + 自定义字段")
    print(f"响应: {result2['messages'][-1].content[:50]}...")
    print(f"自定义字段 user_id: {result2.get('user_id', 'N/A')}")
    print(f"自定义字段 interaction_count: {result2.get('interaction_count', 'N/A')}")
except Exception as e:
    print(f"❌ 错误: {e}")

print()

# ==================== 示例3: 字段验证 ====================
print("=" * 60)
print("示例3: 字段验证测试")
print("=" * 60)

# 测试1: 缺少必需的固定字段
print("\n测试1: 缺少必需的 messages 字段")
try:
    result = agent_custom.invoke({
        "user_id": "user_123",  # 只有自定义字段，没有 messages
    })
    print("❌ 不应该成功")
except Exception as e:
    print(f"✅ 正确捕获错误: {type(e).__name__}")

# 测试2: 传入未定义的自定义字段
print("\n测试2: 传入未在 CustomAgentState 中定义的字段")
try:
    result = agent_custom.invoke({
        "messages": [{"role": "user", "content": "Hello"}],
        "user_id": "user_123",
        "undefined_field": "test",  # 👈 这个字段没有在 CustomAgentState 中定义
    })
    print("✅ 成功（未定义的字段会被忽略，不会报错）")
    print(f"undefined_field 是否在结果中: {'undefined_field' in result}")
except Exception as e:
    print(f"❌ 错误: {e}")

# 测试3: 类型不匹配
print("\n测试3: 自定义字段类型不匹配")
try:
    result = agent_custom.invoke({
        "messages": [{"role": "user", "content": "Hello"}],
        "user_id": 123,  # 👈 应该是字符串，但传入了整数
        "interaction_count": "one",  # 👈 应该是整数，但传入了字符串
    })
    print("⚠️ 类型检查可能不会立即报错（取决于 LangGraph 的实现）")
    print(f"user_id 类型: {type(result.get('user_id'))}")
except Exception as e:
    print(f"✅ 正确捕获类型错误: {type(e).__name__}")

print()

# ==================== 总结 ====================
print("=" * 60)
print("总结")
print("=" * 60)
print("""
固定字段（AgentState 标准字段）:
  ✅ messages: List[BaseMessage]  # 必需
  ✅ next: List[str]              # 可选，通常自动管理

自定义字段（在 CustomAgentState 中定义）:
  ✅ user_id: str
  ✅ user_name: str
  ✅ preferences: dict
  ✅ interaction_count: int

判断方法:
  1. 查看 state_schema 参数指定的类
  2. 该类继承自 AgentState，所以包含所有固定字段
  3. 该类中额外定义的字段就是自定义字段
  4. invoke() 可以传入：固定字段 + 自定义字段
""")

