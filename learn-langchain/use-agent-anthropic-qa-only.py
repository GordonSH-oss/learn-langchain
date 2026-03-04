"""
最简单的 Anthropic 风格问答系统
直接使用 ChatAnthropic 模型进行对话，无需 Agent 框架
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage

# 加载环境变量
load_dotenv()

# 初始化 Anthropic 模型
# 支持自定义 base_url，可以使用代理或第三方兼容服务
model_kwargs = {
    "model": os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-5-sonnet-20241022"),
    "api_key": os.getenv("ANTHROPIC_API_KEY"),
    "temperature": 0.7,
    "max_tokens": 2048
}

# 如果设置了自定义的 base_url，则添加到配置中
base_url = os.getenv("ANTHROPIC_BASE_URL")
if base_url:
    model_kwargs["base_url"] = base_url

model = ChatAnthropic(**model_kwargs)

def simple_chat(question: str, system_prompt: str = None) -> str:
    """
    简单的问答功能
    
    Args:
        question: 用户的问题
        system_prompt: 系统提示词（可选）
    
    Returns:
        AI 的回答
    """
    messages = []
    
    # 添加系统提示词（如果提供）
    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))
    
    # 添加用户问题
    messages.append(HumanMessage(content=question))
    
    # 获取回答
    response = model.invoke(messages)
    return response.content

def chat_with_context(messages_history: list) -> str:
    """
    带上下文的对话
    
    Args:
        messages_history: 消息历史列表，每个元素是 {"role": "user"/"assistant", "content": "..."}
    
    Returns:
        AI 的回答
    """
    from langchain_core.messages import AIMessage
    
    formatted_messages = []
    for msg in messages_history:
        if msg["role"] == "user":
            formatted_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            formatted_messages.append(AIMessage(content=msg["content"]))
        elif msg["role"] == "system":
            formatted_messages.append(SystemMessage(content=msg["content"]))
    
    response = model.invoke(formatted_messages)
    return response.content

if __name__ == "__main__":
    print("=" * 70)
    print("Anthropic 简单问答系统")
    print("=" * 70)
    
    # 定义系统提示词
    system_prompt = """你是一个友好、专业的AI助手。
你的回答应该：
1. 准确、有条理
2. 用简洁明了的语言
3. 如果不确定，请诚实说明
4. 用中文回答中文问题，用英文回答英文问题"""
    
    # 示例1: 简单单次问答
    print("\n【示例1: 简单问答】")
    print("-" * 70)
    
    questions = [
        "你好！请介绍一下你自己。",
        "什么是 LangChain？",
        "Python 的主要优势是什么？"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n问题 {i}: {question}")
        answer = simple_chat(question, system_prompt)
        print(f"回答: {answer}\n")
    
    # 示例2: 带上下文的多轮对话
    print("\n" + "=" * 70)
    print("【示例2: 多轮对话（带上下文）】")
    print("-" * 70)
    
    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "我想学习机器学习，应该从哪里开始？"},
    ]
    
    print(f"\n用户: {conversation[-1]['content']}")
    response1 = chat_with_context(conversation)
    print(f"助手: {response1}\n")
    
    # 继续对话
    conversation.append({"role": "assistant", "content": response1})
    conversation.append({"role": "user", "content": "那我需要先学习哪些数学知识呢？"})
    
    print(f"用户: {conversation[-1]['content']}")
    response2 = chat_with_context(conversation)
    print(f"助手: {response2}\n")
    
    # 继续对话
    conversation.append({"role": "assistant", "content": response2})
    conversation.append({"role": "user", "content": "推荐一些学习资源吧"})
    
    print(f"用户: {conversation[-1]['content']}")
    response3 = chat_with_context(conversation)
    print(f"助手: {response3}\n")
    
    print("=" * 70)
    print("演示完成！")
    print("=" * 70)

