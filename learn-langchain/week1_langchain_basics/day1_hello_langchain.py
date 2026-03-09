"""
Day 1: 环境搭建 & 第一个LangChain应用

学习目标：
1. 理解LangChain生态系统
2. 完成第一个LLM调用
3. 理解消息系统基础
4. 创建简单的问答系统
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ============================================================================
# 配置和初始化
# ============================================================================

# 加载环境变量
load_dotenv()

# 初始化Anthropic模型
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",  # 使用Claude 3.5 Sonnet
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0.7,  # 控制输出的随机性（0-1，越高越随机）
    max_tokens=2048   # 最大输出token数
)

# ============================================================================
# 示例1: 最简单的LLM调用
# ============================================================================

def example1_simple_call():
    """
    最简单的LLM调用
    直接发送一个问题，获取回答
    """
    print("\n" + "="*70)
    print("示例1: 最简单的LLM调用")
    print("="*70)
    
    # 创建一个人类消息
    messages = [HumanMessage(content="你好！请介绍一下自己。")]
    
    # 调用模型
    response = model.invoke(messages)
    
    # 打印回答
    print(f"\n问题: {messages[0].content}")
    print(f"\n回答: {response.content}")
    
    return response

# ============================================================================
# 示例2: 使用系统提示词
# ============================================================================

def example2_with_system_prompt():
    """
    使用系统提示词来设定AI的角色和行为
    """
    print("\n" + "="*70)
    print("示例2: 使用系统提示词")
    print("="*70)
    
    # 定义系统提示词
    system_prompt = """你是一个专业的Python编程助手。
你的特点：
1. 擅长解释Python概念
2. 能提供清晰的代码示例
3. 回答简洁明了
4. 始终保持友好和专业"""
    
    # 构建消息列表
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content="什么是装饰器？请给一个简单的例子。")
    ]
    
    # 调用模型
    response = model.invoke(messages)
    
    print(f"\n系统提示词:\n{system_prompt}")
    print(f"\n问题: {messages[1].content}")
    print(f"\n回答: {response.content}")
    
    return response

# ============================================================================
# 示例3: 多轮对话
# ============================================================================

def example3_conversation():
    """
    实现多轮对话
    保持对话历史，实现上下文理解
    """
    print("\n" + "="*70)
    print("示例3: 多轮对话")
    print("="*70)
    
    # 初始化对话历史
    conversation_history = [
        SystemMessage(content="你是一个友好的AI助手，擅长回答各种问题。")
    ]
    
    # 第一轮对话
    print("\n--- 第1轮对话 ---")
    user_input_1 = "我想学习机器学习，应该从哪里开始？"
    conversation_history.append(HumanMessage(content=user_input_1))
    
    response_1 = model.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response_1.content))
    
    print(f"用户: {user_input_1}")
    print(f"助手: {response_1.content}")
    
    # 第二轮对话（引用上一轮的内容）
    print("\n--- 第2轮对话 ---")
    user_input_2 = "那我需要先学习哪些数学知识呢？"
    conversation_history.append(HumanMessage(content=user_input_2))
    
    response_2 = model.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response_2.content))
    
    print(f"用户: {user_input_2}")
    print(f"助手: {response_2.content}")
    
    # 第三轮对话
    print("\n--- 第3轮对话 ---")
    user_input_3 = "推荐一些学习资源吧"
    conversation_history.append(HumanMessage(content=user_input_3))
    
    response_3 = model.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response_3.content))
    
    print(f"用户: {user_input_3}")
    print(f"助手: {response_3.content}")
    
    return conversation_history

# ============================================================================
# 示例4: 交互式问答系统
# ============================================================================

def example4_interactive_qa():
    """
    创建一个简单的交互式问答系统
    """
    print("\n" + "="*70)
    print("示例4: 交互式问答系统")
    print("="*70)
    print("\n输入 'quit' 或 'exit' 退出\n")
    
    # 系统提示词
    system_prompt = """你是一个友好、专业的AI助手。
你的回答应该：
1. 准确、有条理
2. 用简洁明了的语言
3. 如果不确定，请诚实说明
4. 始终保持友好和专业"""
    
    # 初始化对话历史
    conversation = [SystemMessage(content=system_prompt)]
    
    while True:
        # 获取用户输入
        user_input = input("\n你: ").strip()
        
        # 检查是否退出
        if user_input.lower() in ['quit', 'exit', '退出', 'q']:
            print("\n再见！👋")
            break
        
        # 跳过空输入
        if not user_input:
            continue
        
        # 添加用户消息
        conversation.append(HumanMessage(content=user_input))
        
        # 获取AI回答
        try:
            response = model.invoke(conversation)
            conversation.append(AIMessage(content=response.content))
            
            print(f"\n助手: {response.content}")
            
        except Exception as e:
            print(f"\n❌ 错误: {str(e)}")
            # 移除最后添加的用户消息
            conversation.pop()

# ============================================================================
# 作业示例: 翻译助手
# ============================================================================

def homework_translator():
    """
    作业: 创建一个翻译助手
    
    功能：
    1. 将中文翻译成英文
    2. 将英文翻译成中文
    3. 保持翻译的准确性和自然度
    """
    print("\n" + "="*70)
    print("作业示例: 翻译助手")
    print("="*70)
    
    # TODO: 设计合适的系统提示词
    system_prompt = """你是一个专业的翻译助手。
你的任务：
1. 准确翻译用户输入的文本
2. 如果是中文，翻译成英文
3. 如果是英文，翻译成中文
4. 保持翻译的自然和地道
5. 只返回翻译结果，不需要解释"""
    
    # 测试用例
    test_texts = [
        "你好，世界！",
        "Hello, world!",
        "人工智能正在改变世界。",
        "Machine learning is a subset of artificial intelligence."
    ]
    
    for text in test_texts:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=text)
        ]
        
        response = model.invoke(messages)
        
        print(f"\n原文: {text}")
        print(f"译文: {response.content}")

# ============================================================================
# 知识点总结
# ============================================================================

def knowledge_summary():
    """
    Day 1 知识点总结
    """
    summary = """
    
    ╔══════════════════════════════════════════════════════════════════╗
    ║                       Day 1 知识点总结                             ║
    ╚══════════════════════════════════════════════════════════════════╝
    
    1. LangChain 核心概念
       - LangChain 是一个用于开发LLM应用的框架
       - 提供了统一的接口来调用不同的LLM
       - 简化了复杂AI应用的开发
    
    2. 消息类型
       - SystemMessage: 系统提示词，设定AI角色和行为
       - HumanMessage: 用户输入的消息
       - AIMessage: AI的回答
    
    3. model.invoke()
       - 用于调用LLM模型
       - 接收消息列表作为输入
       - 返回AI的响应
    
    4. 对话历史管理
       - 保持消息列表来维护上下文
       - 按顺序添加用户和AI的消息
       - LLM会根据完整历史来生成回答
    
    5. 参数配置
       - temperature: 控制输出随机性（0-1）
       - max_tokens: 限制输出长度
       - model: 选择使用的模型
    
    6. 最佳实践
       - 使用环境变量管理API Key
       - 编写清晰的系统提示词
       - 处理异常情况
       - 合理管理对话历史（避免过长）
    
    ╔══════════════════════════════════════════════════════════════════╗
    ║                           作业任务                                ║
    ╚══════════════════════════════════════════════════════════════════╝
    
    1. 基础作业：
       - 修改示例2的系统提示词，创建不同性格的AI助手
       - 比如：严肃的老师、幽默的朋友、专业的律师等
    
    2. 进阶作业：
       - 完善翻译助手（homework_translator函数）
       - 添加更多语言支持
       - 实现批量翻译功能
    
    3. 挑战作业：
       - 创建一个"AI面试官"
       - 能够提问并评估回答
       - 保持专业的对话风格
    
    💡 提示：多实验不同的系统提示词，观察AI的行为变化！
    """
    print(summary)

# ============================================================================
# 主函数
# ============================================================================

def main():
    """
    运行所有示例
    """
    print("\n" + "="*70)
    print("🎓 LangChain Day 1: 环境搭建 & 第一个应用")
    print("="*70)
    
    # 检查API Key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("\n❌ 错误: 未找到 ANTHROPIC_API_KEY")
        print("请在项目根目录的 .env 文件中配置 API Key")
        return
    
    print("\n✅ API Key 已配置")
    
    # 运行示例
    try:
        # 示例1: 最简单的调用
        example1_simple_call()
        
        # 示例2: 使用系统提示词
        example2_with_system_prompt()
        
        # 示例3: 多轮对话
        example3_conversation()
        
        # 作业示例: 翻译助手
        homework_translator()
        
        # 知识点总结
        knowledge_summary()
        
        # 示例4: 交互式问答（最后运行，因为会阻塞）
        print("\n" + "="*70)
        print("接下来进入交互式问答模式...")
        print("="*70)
        input("\n按 Enter 继续...")
        
        example4_interactive_qa()
        
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
        print("\n请检查：")
        print("1. API Key 是否正确")
        print("2. 网络连接是否正常")
        print("3. 依赖是否已安装")

if __name__ == "__main__":
    main()
