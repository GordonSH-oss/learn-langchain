"""
测试 Anthropic Agent 的基本功能
确保环境变量配置正确
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def check_env_config():
    """检查环境变量配置"""
    print("=" * 70)
    print("环境变量配置检查")
    print("=" * 70)
    
    api_key = os.getenv('ANTHROPIC_API_KEY')
    base_url = os.getenv('ANTHROPIC_BASE_URL')
    model = os.getenv('ANTHROPIC_MODEL_NAME')
    
    print(f"✓ API Key: {'已设置 (' + api_key[:15] + '...' + api_key[-4:] + ')' if api_key else '❌ 未设置'}")
    print(f"✓ Base URL: {base_url if base_url else '使用默认 (https://api.anthropic.com)'}")
    print(f"✓ Model: {model if model else '使用默认 (claude-3-5-sonnet-20241022)'}")
    print()
    
    if not api_key:
        print("❌ 错误：未设置 ANTHROPIC_API_KEY")
        print("请在 .env 文件中添加：ANTHROPIC_API_KEY=your_key_here")
        return False
    
    return True

def test_simple_chat():
    """测试简单问答功能"""
    try:
        from langchain_anthropic import ChatAnthropic
        from langchain_core.messages import HumanMessage
        
        print("=" * 70)
        print("测试 1: 简单问答")
        print("=" * 70)
        
        # 初始化模型
        model_kwargs = {
            "model": os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-5-sonnet-20241022"),
            "api_key": os.getenv("ANTHROPIC_API_KEY"),
            "temperature": 0.7,
            "max_tokens": 100
        }
        
        base_url = os.getenv("ANTHROPIC_BASE_URL")
        if base_url:
            model_kwargs["base_url"] = base_url
        
        model = ChatAnthropic(**model_kwargs)
        
        # 测试问题
        question = "用一句话介绍你自己"
        print(f"问题: {question}")
        print("-" * 70)
        
        response = model.invoke([HumanMessage(content=question)])
        print(f"回答: {response.content}")
        print()
        
        # 显示 token 使用情况
        usage = response.response_metadata.get('usage', {})
        if usage:
            print(f"Token 使用: 输入={usage.get('input_tokens', 0)}, "
                  f"输出={usage.get('output_tokens', 0)}")
        
        print("✓ 测试通过！")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

def test_with_system_prompt():
    """测试带系统提示词的对话"""
    try:
        from langchain_anthropic import ChatAnthropic
        from langchain_core.messages import HumanMessage, SystemMessage
        
        print("\n" + "=" * 70)
        print("测试 2: 带系统提示词的对话")
        print("=" * 70)
        
        # 初始化模型
        model_kwargs = {
            "model": os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-5-sonnet-20241022"),
            "api_key": os.getenv("ANTHROPIC_API_KEY"),
            "temperature": 0.7,
            "max_tokens": 150
        }
        
        base_url = os.getenv("ANTHROPIC_BASE_URL")
        if base_url:
            model_kwargs["base_url"] = base_url
        
        model = ChatAnthropic(**model_kwargs)
        
        # 测试问题
        system_prompt = "你是一个专业的 Python 编程助手，回答要简洁明了。"
        question = "如何读取 JSON 文件？"
        
        print(f"系统提示: {system_prompt}")
        print(f"问题: {question}")
        print("-" * 70)
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=question)
        ]
        
        response = model.invoke(messages)
        print(f"回答: {response.content}")
        
        print("✓ 测试通过！")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

def test_streaming():
    """测试流式输出"""
    try:
        from langchain_anthropic import ChatAnthropic
        from langchain_core.messages import HumanMessage
        
        print("\n" + "=" * 70)
        print("测试 3: 流式输出")
        print("=" * 70)
        
        # 初始化模型
        model_kwargs = {
            "model": os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-5-sonnet-20241022"),
            "api_key": os.getenv("ANTHROPIC_API_KEY"),
            "temperature": 0.7,
            "max_tokens": 100
        }
        
        base_url = os.getenv("ANTHROPIC_BASE_URL")
        if base_url:
            model_kwargs["base_url"] = base_url
        
        model = ChatAnthropic(**model_kwargs)
        
        question = "数到 10"
        print(f"问题: {question}")
        print("-" * 70)
        print("流式回答: ", end="", flush=True)
        
        for chunk in model.stream([HumanMessage(content=question)]):
            print(chunk.content, end="", flush=True)
        
        print("\n")
        print("✓ 测试通过！")
        return True
        
    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        return False

def main():
    """主测试函数"""
    print("\n🚀 Anthropic Agent 功能测试\n")
    
    # 检查配置
    if not check_env_config():
        print("\n请先配置 .env 文件，参考 ENV_CONFIG_GUIDE.md")
        return
    
    # 运行测试
    tests = [
        ("简单问答", test_simple_chat),
        ("系统提示词", test_with_system_prompt),
        ("流式输出", test_streaming),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"\n❌ {test_name} 测试异常: {str(e)}")
            results.append((test_name, False))
    
    # 总结
    print("\n" + "=" * 70)
    print("测试总结")
    print("=" * 70)
    
    for test_name, success in results:
        status = "✓ 通过" if success else "❌ 失败"
        print(f"{status} - {test_name}")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    print(f"\n通过率: {passed}/{total} ({passed*100//total}%)")
    
    if passed == total:
        print("\n🎉 所有测试通过！系统配置正确。")
    else:
        print("\n⚠️  部分测试失败，请检查配置或网络连接。")

if __name__ == "__main__":
    main()

