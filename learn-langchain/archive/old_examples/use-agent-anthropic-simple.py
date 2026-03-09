"""
最简单的 Anthropic 风格问答 Agent
使用最新的 LangChain API，避免已弃用的导入
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

# 定义系统提示词
SYSTEM_PROMPT = """你是一个有帮助的AI助手。回答用户的问题时要准确、友好、有条理。
如果用户提出数学计算问题，请直接给出答案和计算过程。"""

def chat(question: str, show_details: bool = True) -> str:
    """
    发送问题并获取回答
    
    Args:
        question: 用户的问题
        show_details: 是否显示详细信息
    
    Returns:
        AI 的回答
    """
    try:
        if show_details:
            print(f"\n{'='*60}")
            print(f"问题: {question}")
            print(f"{'='*60}")
        
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=question)
        ]
        
        response = model.invoke(messages)
        
        if show_details:
            # 显示 token 使用情况
            usage = response.response_metadata.get('usage', {})
            if usage:
                print(f"\n[Token 使用] 输入: {usage.get('input_tokens', 0)}, "
                      f"输出: {usage.get('output_tokens', 0)}")
        
        return response.content
        
    except Exception as e:
        error_msg = f"错误: {str(e)}"
        if show_details:
            print(f"\n❌ {error_msg}")
        return error_msg

def chat_with_history(messages_history: list, show_details: bool = True) -> str:
    """
    带上下文的对话
    
    Args:
        messages_history: 消息历史列表
        show_details: 是否显示详细信息
    
    Returns:
        AI 的回答
    """
    from langchain_core.messages import AIMessage
    
    try:
        formatted_messages = [SystemMessage(content=SYSTEM_PROMPT)]
        
        for msg in messages_history:
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                formatted_messages.append(AIMessage(content=msg["content"]))
        
        if show_details:
            print(f"\n{'='*60}")
            print(f"对话轮次: {len(messages_history)}")
            print(f"{'='*60}")
        
        response = model.invoke(formatted_messages)
        return response.content
        
    except Exception as e:
        error_msg = f"错误: {str(e)}"
        if show_details:
            print(f"\n❌ {error_msg}")
        return error_msg

if __name__ == "__main__":
    print("=" * 60)
    print("Anthropic 简单问答 Agent")
    print("=" * 60)
    
    # 测试问题
    test_questions = [
        "你好！请介绍一下你自己。",
        "Python 和 JavaScript 的主要区别是什么？",
        "帮我计算 123 + 456",
        "什么是机器学习？请简单解释。"
    ]
    
    print("\n" + "#" * 60)
    print("# 测试 1: 简单问答")
    print("#" * 60)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{'~'*60}")
        print(f"问题 {i}/{len(test_questions)}")
        print(f"{'~'*60}")
        
        answer = chat(question, show_details=True)
        print(f"\n回答: {answer}")
    
    # 测试多轮对话
    print("\n\n" + "#" * 60)
    print("# 测试 2: 多轮对话（带上下文）")
    print("#" * 60)
    
    conversation = [
        {"role": "user", "content": "我想学习 Python"},
    ]
    
    print(f"\n用户: {conversation[-1]['content']}")
    response1 = chat_with_history(conversation, show_details=True)
    print(f"助手: {response1}\n")
    
    # 继续对话
    conversation.append({"role": "assistant", "content": response1})
    conversation.append({"role": "user", "content": "从哪里开始比较好？"})
    
    print(f"用户: {conversation[-1]['content']}")
    response2 = chat_with_history(conversation, show_details=True)
    print(f"助手: {response2}\n")
    
    print("\n" + "=" * 60)
    print("✅ 测试完成！")
    print("=" * 60)
