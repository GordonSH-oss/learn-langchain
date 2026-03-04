# 如何在实际应用中填充用户信息

## 🤔 问题

在原始代码中，用户信息是手动填入的：

```python
result = agent.invoke({
    "messages": [{"role": "user", "content": "..."}],
    "user_id": "user_123",      # ❌ 用户手动填入？
    "user_name": "Alice",        # ❌ 用户手动填入？
    "preferences": {"theme": "dark"},  # ❌ 用户手动填入？
    "interaction_count": 1,
})
```

**问题：** 在实际应用中，用户交互时不会自己填入这些信息。这些信息应该从哪里来？

## ✅ 解决方案

### 方案1: 从认证系统获取 user_id

**实际应用场景：**
- 用户通过 Web 应用登录
- 系统创建 session 或 JWT token
- 从 session/token 中提取 `user_id`

```python
# Flask 示例
from flask import request, session

@app.route('/api/chat', methods=['POST'])
def chat():
    # 从 session 获取 user_id（用户已登录）
    user_id = session.get('user_id')
    
    # 从请求获取用户消息
    user_message = request.json.get('message')
    
    # 调用 agent（user_id 从 session 获取）
    result = agent.invoke({
        "messages": [{"role": "user", "content": user_message}],
        "user_id": user_id,  # ✅ 从 session 获取
        # ... 其他信息从数据库查询
    })
```

```python
# FastAPI + JWT 示例
from fastapi import Depends, Header
from jose import jwt

def get_current_user(authorization: str = Header(...)):
    """从 JWT token 解析 user_id"""
    token = authorization.replace("Bearer ", "")
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload.get("user_id")

@app.post("/api/chat")
def chat(message: str, user_id: str = Depends(get_current_user)):
    # user_id 自动从 JWT token 获取
    result = agent.invoke({
        "messages": [{"role": "user", "content": message}],
        "user_id": user_id,  # ✅ 从 JWT token 获取
    })
```

### 方案2: 从数据库查询用户信息

**实际应用场景：**
- 有了 `user_id` 后，从数据库查询用户的详细信息
- 包括：`user_name`, `preferences` 等

```python
# 模拟数据库查询函数
def get_user_from_db(user_id: str):
    """从数据库查询用户信息"""
    # 实际应用中应该查询真实数据库
    # SELECT name, preferences FROM users WHERE id = user_id
    return {
        "name": "Alice",
        "preferences": {"theme": "dark", "language": "en"}
    }

# 使用
user_id = session.get('user_id')  # 从认证系统获取
user = get_user_from_db(user_id)  # 从数据库查询

result = agent.invoke({
    "messages": [{"role": "user", "content": user_message}],
    "user_id": user_id,                    # ✅ 从认证系统获取
    "user_name": user["name"],            # ✅ 从数据库查询
    "preferences": user["preferences"],   # ✅ 从数据库查询
})
```

### 方案3: 使用包装函数自动处理（推荐）

**最佳实践：** 创建一个包装函数，自动处理所有逻辑

```python
def chat_with_user(user_message: str, user_id: str, thread_id: str = None):
    """
    自动填充用户信息的包装函数
    
    Args:
        user_message: 用户消息
        user_id: 从认证系统获取（session/JWT token）
        thread_id: 会话ID（可选）
    """
    # 1. 从数据库查询用户信息
    user = get_user_from_db(user_id)
    
    # 2. 自动构建 state
    state = {
        "messages": [{"role": "user", "content": user_message}],
        "user_id": user_id,                    # 从认证系统获取
        "user_name": user["name"],             # 从数据库查询
        "preferences": user["preferences"],    # 从数据库查询
        "interaction_count": 1,                # 可以从历史记录计算
    }
    
    # 3. 调用 agent
    config = {"configurable": {"thread_id": thread_id or f"thread_{user_id}"}}
    return agent.invoke(state, config=config)

# 使用（非常简单）
user_id = session.get('user_id')  # 从认证系统获取
result = chat_with_user(
    user_message="Hello",
    user_id=user_id,  # 只需要传入 user_id，其他自动处理
)
```

### 方案4: 从消息中提取信息（可选）

**高级场景：** Agent 可以从用户消息中智能提取信息

```python
# 用户说："My name is Alice and I prefer dark theme"
# Agent 可以提取：name="Alice", theme="dark"

# 方式1: 使用 LLM 提取
def extract_user_info(user_message: str):
    """使用 LLM 从消息中提取用户信息"""
    prompt = f"""
    从以下消息中提取用户信息：
    {user_message}
    
    返回 JSON 格式：{{"name": "...", "preferences": {{...}}}}
    """
    # 调用 LLM 提取信息
    # ...

# 方式2: Agent 自动提取（如果配置了相关工具）
# Agent 可以调用 save_user_preference 工具来更新偏好
```

## 📊 完整流程对比

### ❌ 错误方式（原始代码）

```python
# 用户需要手动填入所有信息
result = agent.invoke({
    "messages": [{"role": "user", "content": "Hello"}],
    "user_id": "user_123",           # ❌ 用户手动填入
    "user_name": "Alice",            # ❌ 用户手动填入
    "preferences": {"theme": "dark"}, # ❌ 用户手动填入
    "interaction_count": 1,         # ❌ 用户手动填入
})
```

**问题：**
- 用户不知道自己的 `user_id`
- 用户信息应该从数据库查询
- 不安全（用户可以伪造信息）

### ✅ 正确方式（改进代码）

```python
# 1. 从认证系统获取 user_id
user_id = session.get('user_id')  # 或从 JWT token 解析

# 2. 从数据库查询用户信息
user = get_user_from_db(user_id)

# 3. 调用包装函数（自动处理）
result = chat_with_user(
    user_message="Hello",
    user_id=user_id,  # ✅ 从认证系统获取
    # 其他信息自动从数据库查询
)
```

**优点：**
- ✅ 安全（用户无法伪造信息）
- ✅ 自动化（不需要手动填入）
- ✅ 一致（所有信息来自单一数据源）

## 🔄 实际应用中的完整流程

```
用户登录
  ↓
系统创建 session/JWT token
  ↓
用户发送消息到 /api/chat
  ↓
后端从 session/token 提取 user_id
  ↓
从数据库查询用户信息（user_name, preferences）
  ↓
调用 chat_with_user() 包装函数
  ↓
自动构建 state（包含所有用户信息）
  ↓
调用 agent.invoke()
  ↓
返回响应给用户
```

## 📝 代码示例

### 完整示例1: Flask 应用

```python
from flask import Flask, request, session
from use_agent_with_memory_improved import chat_with_user

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    # 1. 检查用户是否登录
    user_id = session.get('user_id')
    if not user_id:
        return {'error': 'Not authenticated'}, 401
    
    # 2. 获取用户消息
    data = request.json
    user_message = data.get('message')
    
    # 3. 调用自动填充函数
    result = chat_with_user(
        user_message=user_message,
        user_id=user_id,  # ✅ 从 session 获取
        thread_id=f"thread_{user_id}"
    )
    
    # 4. 返回响应
    return {
        'response': result['messages'][-1].content,
        'user_name': result.get('user_name'),
        'preferences': result.get('preferences')
    }

@app.route('/api/login', methods=['POST'])
def login():
    """登录接口，设置 session"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # 验证用户名密码（实际应用中应该查询数据库）
    if username == 'alice' and password == 'password':
        user_id = 'user_123'  # 从数据库查询
        session['user_id'] = user_id  # 设置 session
        return {'success': True, 'user_id': user_id}
    return {'error': 'Invalid credentials'}, 401
```

### 完整示例2: FastAPI + JWT

```python
from fastapi import FastAPI, Depends, Header, HTTPException
from jose import jwt, JWTError
from use_agent_with_memory_improved import chat_with_user

app = FastAPI()
SECRET_KEY = "your-secret-key"

def get_current_user(authorization: str = Header(...)):
    """从 JWT token 解析 user_id"""
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/api/chat")
def chat_endpoint(
    message: str,
    user_id: str = Depends(get_current_user)  # ✅ 自动从 JWT token 获取
):
    """聊天接口"""
    result = chat_with_user(
        user_message=message,
        user_id=user_id,  # ✅ 从 JWT token 自动获取
        thread_id=f"thread_{user_id}"
    )
    return {"response": result['messages'][-1].content}
```

## 🎯 关键要点总结

1. **user_id** → 从认证系统获取（session/JWT token）
2. **user_name** → 从数据库查询（根据 user_id）
3. **preferences** → 从数据库查询（根据 user_id）
4. **interaction_count** → 可以从历史记录计算
5. **使用包装函数** → 封装所有逻辑，简化调用

## 📚 相关文件

- `use-agent-with-memory-improved.py` - 改进版本的完整代码
- `use-agent-with-memory-realistic.py` - 更详细的实现示例
- `use-agent-with-memory-1.py` - 原始代码（仅用于学习）

