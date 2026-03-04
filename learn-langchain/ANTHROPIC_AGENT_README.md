# Anthropic 风格问答 Agent 使用指南

本目录包含两个使用 Anthropic Claude 模型的简单问答 Agent 示例。

## 文件说明

### 1. `use-agent-anthropic-qa-only.py` ⭐ 推荐
最简单的纯问答系统，直接使用 ChatAnthropic 模型，无需 Agent 框架。

**特点：**
- ✅ 代码简洁，易于理解
- ✅ 支持单次问答
- ✅ 支持多轮对话（带上下文）
- ✅ 适合快速开始

**使用场景：**
- 纯粹的问答对话
- 不需要调用外部工具
- 需要保持对话上下文

### 2. `use-agent-anthropic-simple.py`
使用 LangChain 的 Agent 框架（ReAct 模式），支持工具调用。

**特点：**
- ✅ 完整的 Agent 框架
- ✅ 支持工具集成（示例：计算器）
- ✅ ReAct 推理模式
- ✅ 适合需要扩展功能的场景

**使用场景：**
- 需要调用外部工具或 API
- 需要 Agent 的推理和规划能力
- 复杂的多步骤任务

## 环境配置

### 1. 安装依赖

```bash
pip install langchain langchain-anthropic python-dotenv
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件：

```bash
# Anthropic API 配置
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# 可选：自定义 API 端点（用于代理或第三方兼容服务）
ANTHROPIC_BASE_URL=https://api.anthropic.com

# 可选：指定模型名称
ANTHROPIC_MODEL_NAME=claude-3-5-sonnet-20241022
```

### 3. 获取 API Key

#### 方式1：官方 Anthropic API
1. 访问 [Anthropic Console](https://console.anthropic.com/)
2. 注册并登录账号
3. 进入 API Keys 页面
4. 创建新的 API Key
5. 复制到 `.env` 文件中

#### 方式2：使用代理或第三方服务
如果你使用代理服务或第三方兼容的 API 服务，需要同时设置：
```bash
ANTHROPIC_API_KEY=your_proxy_api_key
ANTHROPIC_BASE_URL=https://your-proxy-url.com/v1
```

## 支持的模型

在 `.env` 文件中设置 `ANTHROPIC_MODEL_NAME`，可选值：

| 模型名称 | 说明 | 适用场景 |
|---------|------|---------|
| `claude-3-5-sonnet-20241022` | Claude 3.5 Sonnet（推荐） | 平衡性能和成本 |
| `claude-3-opus-20240229` | Claude 3 Opus | 最强性能，适合复杂任务 |
| `claude-3-sonnet-20240229` | Claude 3 Sonnet | 性价比高 |
| `claude-3-haiku-20240307` | Claude 3 Haiku | 最快速度，低成本 |

## 快速开始

### 示例1：简单问答（推荐新手）

```bash
python use-agent-anthropic-qa-only.py
```

**代码示例：**

```python
from use_agent_anthropic_qa_only import simple_chat

# 单次问答
answer = simple_chat("什么是 LangChain？")
print(answer)
```

### 示例2：多轮对话

```python
from use_agent_anthropic_qa_only import chat_with_context

conversation = [
    {"role": "system", "content": "你是一个友好的 AI 助手"},
    {"role": "user", "content": "介绍一下 Python"},
]

response = chat_with_context(conversation)
print(response)

# 继续对话
conversation.append({"role": "assistant", "content": response})
conversation.append({"role": "user", "content": "它有什么优势？"})

response2 = chat_with_context(conversation)
print(response2)
```

### 示例3：使用 Agent 框架（带工具）

```bash
python use-agent-anthropic-simple.py
```

**代码示例：**

```python
from use_agent_anthropic_simple import chat

# Agent 会自动决定是否使用工具
answer = chat("帮我计算 123 + 456")
print(answer)
```

## 配置参数说明

### 模型参数

在代码中可以调整以下参数：

```python
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",  # 模型名称
    api_key=os.getenv("ANTHROPIC_API_KEY"),  # API Key
    base_url=os.getenv("ANTHROPIC_BASE_URL"),  # 自定义端点（可选）
    temperature=0.7,  # 温度：0-1，越高越随机
    max_tokens=2048,  # 最大输出 token 数
)
```

### Temperature 说明
- `0.0`: 最确定性，适合需要一致性答案的场景
- `0.5`: 平衡创造性和一致性
- `0.7`: 推荐值，适合日常对话
- `1.0`: 最大创造性，适合创意写作

## 常见问题

### Q1: 如何处理 API 超时？
```python
model = ChatAnthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    timeout=60,  # 设置超时时间（秒）
    max_retries=3,  # 最大重试次数
)
```

### Q2: 如何流式输出？
```python
for chunk in model.stream("你好"):
    print(chunk.content, end="", flush=True)
```

### Q3: 如何查看 API 消耗？
```python
response = model.invoke([HumanMessage(content="Hello")])
print(f"输入 tokens: {response.response_metadata.get('usage', {}).get('input_tokens')}")
print(f"输出 tokens: {response.response_metadata.get('usage', {}).get('output_tokens')}")
```

### Q4: 支持异步调用吗？
```python
import asyncio

async def async_chat():
    response = await model.ainvoke([HumanMessage(content="Hello")])
    return response.content

result = asyncio.run(async_chat())
```

## 进阶使用

### 自定义系统提示词

```python
system_prompt = """你是一个专业的 Python 编程助手。
你的回答应该：
1. 提供可运行的代码示例
2. 解释代码的工作原理
3. 指出潜在的问题和最佳实践
4. 使用中文回答"""

answer = simple_chat("如何读取 JSON 文件？", system_prompt)
```

### 添加自定义工具

在 `use-agent-anthropic-simple.py` 中添加工具：

```python
@tool
def search_weather(city: str) -> str:
    """查询城市天气"""
    # 实现天气查询逻辑
    return f"{city} 的天气是晴天"

tools = [
    Tool(
        name="SearchWeather",
        func=search_weather,
        description="查询指定城市的天气信息"
    )
]
```

## 性能优化建议

1. **使用合适的模型**：根据任务复杂度选择模型
2. **控制 token 使用**：设置合理的 `max_tokens`
3. **缓存系统提示词**：减少重复输入
4. **批量处理**：合并多个简单请求
5. **使用流式输出**：提升用户体验

## 错误处理

```python
from langchain_core.exceptions import LangChainException

try:
    response = model.invoke([HumanMessage(content="Hello")])
except LangChainException as e:
    print(f"LangChain 错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
```

## 相关资源

- [Anthropic 官方文档](https://docs.anthropic.com/)
- [LangChain 文档](https://python.langchain.com/)
- [Claude 模型对比](https://www.anthropic.com/claude)
- [LangChain Anthropic 集成](https://python.langchain.com/docs/integrations/chat/anthropic)

## 许可和使用限制

请遵守 Anthropic 的使用条款和 API 限制：
- 注意 API 调用频率限制
- 遵守内容政策
- 合理使用配额

---

**提示**: 建议先从 `use-agent-anthropic-qa-only.py` 开始，熟悉基本用法后再尝试 Agent 框架。

