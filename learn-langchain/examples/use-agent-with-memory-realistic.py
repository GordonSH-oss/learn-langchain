"""
实际应用场景：如何自动填充用户信息

在实际应用中，用户信息应该从以下来源自动获取：
1. 用户会话/认证系统（session, JWT token）
2. 数据库查询（根据 user_id 查询用户信息）
3. 从消息中提取（Agent 智能提取用户信息）
4. 中间件自动填充
"""

import os
from dotenv import load_dotenv
from langchain.agents import create_agent, AgentState
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from typing import Optional, Dict, Any

load_dotenv()

# ==================== 模拟数据库/用户服务 ====================
class UserService:
    """模拟用户服务，实际应用中应该连接真实数据库"""
    
    # 模拟用户数据库
    _users_db = {
        "user_123": {
            "name": "Alice",
            "email": "alice@example.com",
            "preferences": {"theme": "dark", "language": "en"},
            "created_at": "2024-01-01"
        },
        "user_456": {
            "name": "Bob",
            "email": "bob@example.com",
            "preferences": {"theme": "light", "language": "zh"},
            "created_at": "2024-01-02"
        }
    }
    
    @classmethod
    def get_user_by_id(cls, user_id: str) -> Optional[Dict[str, Any]]:
        """根据 user_id 查询用户信息"""
        return cls._users_db.get(user_id)
    
    @classmethod
    def get_user_by_session(cls, session_id: str) -> Optional[Dict[str, Any]]:
        """根据 session_id 查询用户信息（模拟）"""
        # 实际应用中，session_id 会映射到 user_id
        session_to_user = {
            "session_001": "user_123",
            "session_002": "user_456",
        }
        user_id = session_to_user.get(session_id)
        if user_id:
            return cls.get_user_by_id(user_id)
        return None
    
    @classmethod
    def update_user_preference(cls, user_id: str, key: str, value: Any):
        """更新用户偏好"""
        if user_id in cls._users_db:
            cls._users_db[user_id]["preferences"][key] = value
            return True
        return False


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
    user = UserService.get_user_by_id(user_id)
    if user:
        return f"User: {user['name']}, Email: {user['email']}, Preferences: {user['preferences']}"
    return f"User {user_id} not found"


@tool
def save_user_preference(user_id: str, key: str, value: str) -> str:
    """保存用户偏好"""
    if UserService.update_user_preference(user_id, key, value):
        return f"Saved preference: {user_id} - {key}: {value}"
    return f"Failed to save preference for user {user_id}"


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


# ==================== 方法1: 从会话/认证系统获取用户信息 ====================
def invoke_with_session(user_message: str, session_id: str, thread_id: str = None):
    """
    方法1: 从会话系统自动获取用户信息
    
    在实际应用中：
    - session_id 来自 HTTP session 或 JWT token
    - 从 session 中获取 user_id
    - 从数据库查询用户详细信息
    """
    # 1. 从 session 获取 user_id（实际应用中从 session/token 中提取）
    user = UserService.get_user_by_session(session_id)
    
    if not user:
        raise ValueError(f"Session {session_id} not found or user not authenticated")
    
    # 2. 从数据库查询用户信息
    user_id = None
    for uid, user_data in UserService._users_db.items():
        if user_data == user:
            user_id = uid
            break
    
    # 3. 从 checkpoint 获取历史状态（如果有）
    if thread_id:
        # 尝试从 checkpoint 恢复状态
        try:
            # 这里简化处理，实际应该从 checkpointer 读取
            interaction_count = 1  # 实际应该从历史记录计算
        except:
            interaction_count = 1
    else:
        interaction_count = 1
    
    # 4. 自动构建 state
    state = {
        "messages": [{"role": "user", "content": user_message}],
        "user_id": user_id,
        "user_name": user["name"],
        "preferences": user["preferences"].copy(),
        "interaction_count": interaction_count,
    }
    
    # 5. 调用 agent
    config = {"configurable": {"thread_id": thread_id or f"thread_{user_id}"}}
    return agent.invoke(state, config=config)


# ==================== 方法2: 从消息中提取用户信息（智能提取）====================
def invoke_with_extraction(user_message: str, user_id: str, thread_id: str = None):
    """
    方法2: 从用户消息中智能提取信息
    
    实际应用中：
    - Agent 可以从消息中提取用户信息（如 "My name is Alice"）
    - 结合已有的用户信息（从数据库查询）
    - 更新用户偏好
    """
    # 1. 从数据库获取基础用户信息
    user = UserService.get_user_by_id(user_id)
    
    if not user:
        # 如果是新用户，创建默认信息
        user = {
            "name": "Unknown",
            "preferences": {},
        }
    
    # 2. 让 Agent 从消息中提取信息（这里简化，实际可以用 NER 或 LLM 提取）
    # 实际应用中，可以先用一个 LLM 调用提取信息，然后再调用 agent
    
    # 3. 构建 state（基础信息 + 从消息中提取的信息）
    state = {
        "messages": [{"role": "user", "content": user_message}],
        "user_id": user_id,
        "user_name": user["name"],
        "preferences": user["preferences"].copy(),
        "interaction_count": 1,
    }
    
    # 4. 调用 agent
    config = {"configurable": {"thread_id": thread_id or f"thread_{user_id}"}}
    result = agent.invoke(state, config=config)
    
    # 5. 从 Agent 的响应中提取并更新用户信息（如果需要）
    # 这里简化处理，实际应该解析 Agent 的响应
    
    return result


# ==================== 方法3: 使用包装函数自动填充 ====================
def create_agent_wrapper(agent_instance, user_service: UserService):
    """
    方法3: 创建一个包装函数，自动处理用户信息填充
    
    这是最推荐的方式，在实际应用中应该这样使用
    """
    def invoke(user_message: str, user_id: str = None, session_id: str = None, 
               thread_id: str = None, **kwargs):
        """
        自动填充用户信息的 invoke 包装函数
        
        Args:
            user_message: 用户消息
            user_id: 用户ID（优先使用）
            session_id: 会话ID（如果没有 user_id，则从 session 获取）
            thread_id: 线程ID（用于记忆）
            **kwargs: 其他自定义字段
        """
        # 1. 确定 user_id
        if not user_id and session_id:
            user = user_service.get_user_by_session(session_id)
            if user:
                # 找到对应的 user_id
                for uid, user_data in user_service._users_db.items():
                    if user_data == user:
                        user_id = uid
                        break
        
        if not user_id:
            raise ValueError("Must provide either user_id or session_id")
        
        # 2. 从数据库获取用户信息
        user = user_service.get_user_by_id(user_id)
        
        if not user:
            # 新用户，使用默认值
            user = {
                "name": "User",
                "preferences": {},
            }
        
        # 3. 从 checkpoint 获取历史状态
        interaction_count = kwargs.get("interaction_count", 1)
        if thread_id:
            # 实际应用中应该从 checkpointer 读取历史状态
            # 这里简化处理
            pass
        
        # 4. 合并用户信息和自定义字段
        state = {
            "messages": [{"role": "user", "content": user_message}],
            "user_id": user_id,
            "user_name": user["name"],
            "preferences": user["preferences"].copy(),
            "interaction_count": interaction_count,
            **kwargs  # 允许覆盖或添加其他字段
        }
        
        # 5. 调用 agent
        config = {"configurable": {"thread_id": thread_id or f"thread_{user_id}"}}
        return agent_instance.invoke(state, config=config)
    
    return invoke


# ==================== 使用示例 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("实际应用场景：自动填充用户信息")
    print("=" * 60)
    
    # ========== 场景1: 从 session 获取用户信息 ==========
    print("\n【场景1】从 session 获取用户信息")
    print("-" * 60)
    print("用户发送消息: 'Hi, what's my preferred theme?'")
    print("系统自动从 session 获取用户信息...")
    
    try:
        result1 = invoke_with_session(
            user_message="Hi, what's my preferred theme?",
            session_id="session_001",  # 从 HTTP session 或 JWT token 获取
            thread_id="thread_001"
        )
        print(f"✅ Agent 响应: {result1['messages'][-1].content[:100]}...")
        print(f"✅ 自动填充的用户信息:")
        print(f"   - user_id: {result1.get('user_id')}")
        print(f"   - user_name: {result1.get('user_name')}")
        print(f"   - preferences: {result1.get('preferences')}")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    # ========== 场景2: 从 user_id 查询用户信息 ==========
    print("\n【场景2】从 user_id 查询用户信息")
    print("-" * 60)
    print("用户发送消息: 'Hello, I'm Bob'")
    print("系统根据 user_id 从数据库查询用户信息...")
    
    try:
        result2 = invoke_with_extraction(
            user_message="Hello, I'm Bob",
            user_id="user_456",  # 从认证系统获取（如 JWT token）
            thread_id="thread_002"
        )
        print(f"✅ Agent 响应: {result2['messages'][-1].content[:100]}...")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    # ========== 场景3: 使用包装函数（推荐方式）==========
    print("\n【场景3】使用包装函数（推荐方式）")
    print("-" * 60)
    print("用户发送消息: 'Save my language preference as Chinese'")
    print("使用包装函数自动处理...")
    
    agent_invoke = create_agent_wrapper(agent, UserService)
    
    try:
        result3 = agent_invoke(
            user_message="Save my language preference as Chinese",
            user_id="user_123",  # 从认证系统获取
            thread_id="thread_001"
        )
        print(f"✅ Agent 响应: {result3['messages'][-1].content[:100]}...")
        print(f"✅ 更新后的偏好: {UserService.get_user_by_id('user_123')['preferences']}")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    # ========== 场景4: Web 应用示例（伪代码）==========
    print("\n【场景4】Web 应用集成示例（伪代码）")
    print("-" * 60)
    print("""
    # Flask/FastAPI 示例
    from flask import request, session
    
    @app.route('/chat', methods=['POST'])
    def chat():
        # 1. 从 session 或 JWT token 获取 user_id
        user_id = session.get('user_id')  # 或从 JWT 解析
        
        # 2. 从请求中获取用户消息
        user_message = request.json.get('message')
        
        # 3. 使用包装函数自动填充用户信息
        agent_invoke = create_agent_wrapper(agent, UserService)
        result = agent_invoke(
            user_message=user_message,
            user_id=user_id,
            thread_id=f"thread_{user_id}"  # 使用 user_id 作为 thread_id
        )
        
        # 4. 返回响应
        return {'response': result['messages'][-1].content}
    """)
    
    print("\n" + "=" * 60)
    print("总结")
    print("=" * 60)
    print("""
在实际应用中，用户信息应该：

1. ✅ 从认证系统获取（session, JWT token）
   → 获取 user_id
   
2. ✅ 从数据库查询（根据 user_id）
   → 获取 user_name, preferences 等
   
3. ✅ 从消息中提取（可选，Agent 智能提取）
   → 更新用户信息
   
4. ✅ 使用包装函数自动处理
   → 封装所有逻辑，简化调用

❌ 不应该：用户手动传入这些信息
✅ 应该：系统自动从认证/数据库获取
    """)

