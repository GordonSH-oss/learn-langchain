"""
改进版本：展示如何在实际应用中自动填充用户信息

关键改进：
1. 从认证系统获取 user_id（而不是硬编码）
2. 从数据库查询用户信息（而不是手动填入）
3. 使用包装函数简化调用
"""

import os
from dotenv import load_dotenv
from langchain.agents import create_agent, AgentState
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

# ==================== 模拟用户数据库 ====================
# 实际应用中，这应该是一个真实的数据库查询
USER_DATABASE = {
    "user_123": {
        "name": "Alice",
        "preferences": {"theme": "dark", "language": "en"}
    },
    "user_456": {
        "name": "Bob",
        "preferences": {"theme": "light", "language": "zh"}
    }
}

def get_user_from_db(user_id: str):
    """从数据库获取用户信息（实际应用中应该查询真实数据库）"""
    return USER_DATABASE.get(user_id, {
        "name": "Unknown",
        "preferences": {}
    })


# ==================== 定义自定义 State ====================
class CustomAgentState(AgentState):
    """扩展 AgentState 添加自定义字段"""
    user_id: str
    user_name: str
    preferences: dict
    interaction_count: int


# ==================== 定义工具 ====================
@tool
def get_user_profile(user_id: str) -> str:
    """获取用户档案"""
    user = get_user_from_db(user_id)
    return f"User: {user.get('name', 'Unknown')}, Prefs: {user.get('preferences', {})}"


@tool
def save_user_preference(user_id: str, key: str, value: str) -> str:
    """保存用户偏好"""
    if user_id in USER_DATABASE:
        USER_DATABASE[user_id]["preferences"][key] = value
        return f"Saved preference: {user_id} - {key}: {value}"
    return f"User {user_id} not found"


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
    state_schema=CustomAgentState,
    checkpointer=InMemorySaver(),
)


# ==================== 关键改进：自动填充用户信息的函数 ====================
def chat_with_user(user_message: str, user_id: str, thread_id: str = None):
    """
    实际应用中应该使用的函数
    
    这个函数会自动：
    1. 从数据库查询用户信息
    2. 构建完整的 state
    3. 调用 agent
    
    用户只需要传入：
    - user_message: 用户消息
    - user_id: 从认证系统获取（session/JWT token）
    - thread_id: 会话ID（可选）
    """
    # ✅ 步骤1: 从数据库自动获取用户信息（而不是手动填入）
    user = get_user_from_db(user_id)
    
    # ✅ 步骤2: 自动构建 state
    state = {
        "messages": [{"role": "user", "content": user_message}],
        "user_id": user_id,                                    # 从认证系统获取
        "user_name": user["name"],                            # 从数据库查询
        "preferences": user["preferences"].copy(),            # 从数据库查询
        "interaction_count": 1,                               # 可以从历史记录计算
    }
    
    # ✅ 步骤3: 调用 agent
    config = {"configurable": {"thread_id": thread_id or f"thread_{user_id}"}}
    return agent.invoke(state, config=config)


# ==================== 使用示例 ====================
if __name__ == "__main__":
    thread_id = "thread_001"
    
    print("=" * 60)
    print("改进版本：自动填充用户信息")
    print("=" * 60)
    
    # ========== 第一次交互 ==========
    print("\n=== 第一次交互 ===")
    print("用户发送: 'Hi, my name is Alice and I prefer dark theme'")
    print("系统自动从数据库查询用户信息...")
    
    # ✅ 实际应用中，user_id 应该从认证系统获取（如 session/JWT token）
    # 这里模拟从认证系统获取的 user_id
    authenticated_user_id = "user_123"  # 👈 从 session/JWT token 获取
    
    result1 = chat_with_user(
        user_message="Hi, my name is Alice and I prefer dark theme",
        user_id=authenticated_user_id,  # 👈 从认证系统获取，不是用户手动填入
        thread_id=thread_id
    )
    
    print(f"\n✅ Agent 响应: {result1['messages'][-1].content}")
    print(f"✅ 自动填充的信息:")
    print(f"   - user_id: {result1.get('user_id')} (从认证系统获取)")
    print(f"   - user_name: {result1.get('user_name')} (从数据库查询)")
    print(f"   - preferences: {result1.get('preferences')} (从数据库查询)")
    print()
    
    # ========== 第二次交互 ==========
    print("=== 第二次交互（同一线程） ===")
    print("用户发送: 'What theme do you think I prefer?'")
    print("系统自动从数据库查询用户信息，Agent 记得之前的对话...")
    
    result2 = chat_with_user(
        user_message="What theme do you think I prefer?",
        user_id=authenticated_user_id,  # 👈 同样从认证系统获取
        thread_id=thread_id  # 👈 使用相同的 thread_id，Agent 会记住之前的对话
    )
    
    print(f"\n✅ Agent 响应: {result2['messages'][-1].content}")
    print(f"✅ 消息历史长度: {len(result2['messages'])} (包含之前的对话)")
    print()
    
    # ========== 第三次交互 ==========
    print("=== 第三次交互（同一线程） ===")
    print("用户发送: 'Save my language preference as Chinese'")
    
    result3 = chat_with_user(
        user_message="Save my language preference as Chinese",
        user_id=authenticated_user_id,
        thread_id=thread_id
    )
    
    print(f"\n✅ Agent 响应: {result3['messages'][-1].content}")
    print(f"✅ 更新后的用户偏好: {get_user_from_db(authenticated_user_id)['preferences']}")
    print()
    
    # ========== Web 应用集成示例 ==========
    print("=" * 60)
    print("Web 应用集成示例（伪代码）")
    print("=" * 60)
    print("""
    # Flask 示例
    from flask import request, session
    
    @app.route('/api/chat', methods=['POST'])
    def chat_endpoint():
        # 1. 从 session 获取 user_id（用户已登录）
        user_id = session.get('user_id')
        if not user_id:
            return {'error': 'Not authenticated'}, 401
        
        # 2. 从请求中获取用户消息
        data = request.json
        user_message = data.get('message')
        
        # 3. 调用自动填充函数（不需要手动填入用户信息）
        result = chat_with_user(
            user_message=user_message,
            user_id=user_id,  # 👈 从 session 获取
            thread_id=f"thread_{user_id}"  # 👈 使用 user_id 作为 thread_id
        )
        
        # 4. 返回响应
        return {
            'response': result['messages'][-1].content,
            'user_name': result.get('user_name'),
            'preferences': result.get('preferences')
        }
    
    # FastAPI 示例
    from fastapi import FastAPI, Depends, Header
    from jose import jwt  # JWT token 解析
    
    def get_current_user(authorization: str = Header(...)):
        # 从 JWT token 解析 user_id
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload.get("user_id")
    
    @app.post("/api/chat")
    def chat_endpoint(message: str, user_id: str = Depends(get_current_user)):
        # user_id 自动从 JWT token 获取
        result = chat_with_user(
            user_message=message,
            user_id=user_id,  # 👈 从 JWT token 自动获取
            thread_id=f"thread_{user_id}"
        )
        return {"response": result['messages'][-1].content}
    """)
    
    print("\n" + "=" * 60)
    print("关键点总结")
    print("=" * 60)
    print("""
❌ 错误方式（原始代码）:
    agent.invoke({
        "messages": [...],
        "user_id": "user_123",      # 👈 用户手动填入
        "user_name": "Alice",        # 👈 用户手动填入
        "preferences": {...},        # 👈 用户手动填入
    })

✅ 正确方式（改进代码）:
    # 1. 从认证系统获取 user_id
    user_id = session.get('user_id')  # 或从 JWT token 解析
    
    # 2. 调用自动填充函数
    result = chat_with_user(
        user_message="Hello",
        user_id=user_id,  # 👈 从认证系统获取
        # 其他信息自动从数据库查询
    )

关键改进：
1. ✅ user_id 从认证系统获取（session/JWT token）
2. ✅ user_name 从数据库查询（根据 user_id）
3. ✅ preferences 从数据库查询（根据 user_id）
4. ✅ interaction_count 可以从历史记录计算
5. ✅ 使用包装函数封装所有逻辑
    """)

