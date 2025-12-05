import os
from dotenv import load_dotenv
from langchain.agents import create_agent, AgentState
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
import uuid

# 加载环境变量
load_dotenv()

# ==================== 定义自定义 State ====================
class CustomAgentState(AgentState):
    """扩展 AgentState 添加自定义字段"""
    user_id: str  # 用户 ID
    user_name: str  # 用户名
    preferences: dict  # 用户偏好
    interaction_count: int  # 交互次数


# ==================== 定义工具 ====================
@tool
def get_user_profile(user_id: str) -> str:
    """获取用户档案"""
    profiles = {
        "user_123": {"name": "Alice", "preferences": {"theme": "dark", "language": "en"}},
        "user_456": {"name": "Bob", "preferences": {"theme": "light", "language": "zh"}},
    }
    profile = profiles.get(user_id, {})
    return f"User: {profile.get('name', 'Unknown')}, Prefs: {profile.get('preferences', {})}"


@tool
def save_user_preference(user_id: str, key: str, value: str) -> str:
    """保存用户偏好"""
    return f"Saved preference: {user_id} - {key}: {value}"


# ==================== 创建 Agent ====================
model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

agent = create_agent(
    model=model,
    tools=[get_user_profile, save_user_preference],
    system_prompt="You are a helpful assistant that remembers user preferences. Always consider the user's preferences when making recommendations.",
    state_schema=CustomAgentState,  # 使用自定义 State
    checkpointer=InMemorySaver(),   # 持久化短期记忆
)

# ==================== 使用 Agent ====================
# 第一次交互
thread_id = "thread_001"  # 同一个用户的会话 ID

print("=== 第一次交互 ===")
result1 = agent.invoke(
    {
        "messages": [{"role": "user", "content": "Hi, my name is Alice and I prefer dark theme"}],
        "user_id": "user_123",
        "user_name": "Alice",
        "preferences": {"theme": "dark"},
        "interaction_count": 1,
    },
    config={"configurable": {"thread_id": thread_id}}
)

print("Agent Response:", result1["messages"][-1].content)
print(f"Interaction Count: {result1.get('interaction_count', 0)}")
print()

# 第二次交互（同一线程，Agent 记得之前的信息）
print("=== 第二次交互（同一线程） ===")
result2 = agent.invoke(
    {
        "messages": [{"role": "user", "content": "What theme do you think I prefer?"}],
        "user_id": "user_123",
        "user_name": "Alice",
        "preferences": {"theme": "dark"},
        "interaction_count": 2,
    },
    config={"configurable": {"thread_id": thread_id}}
)

print("Agent Response:", result2["messages"][-1].content)
print(f"Message History Length: {len(result2['messages'])}")  # 应该有更多消息
print()

# 第三次交互
print("=== 第三次交互（同一线程） ===")
result3 = agent.invoke(
    {
        "messages": [{"role": "user", "content": "Save my language preference as Chinese"}],
        "user_id": "user_123",
        "user_name": "Alice",
        "preferences": {"theme": "dark", "language": "zh"},
        "interaction_count": 3,
    },
    config={"configurable": {"thread_id": thread_id}}
)

print("Agent Response:", result3["messages"][-1].content)
print()