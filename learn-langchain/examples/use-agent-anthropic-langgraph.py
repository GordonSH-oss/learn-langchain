"""
简单的 Anthropic 风格问答 Agent
直接使用 LangGraph 和 ChatAnthropic 模型（兼容新版 LangChain）
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool
from typing import Annotated, Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, MessagesState
from langgraph.prebuilt import ToolNode

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

# 创建一个简单的工具（可选，这里只是为了展示框架）
@tool
def simple_calculator(expression: str) -> str:
    """执行简单的数学计算。输入应该是一个数学表达式，例如: '2+2' 或 '10*5'"""
    try:
        # 安全地计算数学表达式
        result = eval(expression, {"__builtins__": {}}, {})
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

# 定义工具列表
tools = [simple_calculator]

# 将工具绑定到模型
model_with_tools = model.bind_tools(tools)

# 定义 Agent 节点
def call_model(state: MessagesState):
    """调用模型并返回响应"""
    system_message = SystemMessage(
        content="""你是一个有帮助的AI助手。回答用户的问题时要准确、友好、有条理。

你有以下工具可以使用：
- simple_calculator: 执行简单的数学计算

如果用户问数学问题，使用计算器工具；否则直接回答问题。"""
    )
    messages = [system_message] + state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

# 定义路由函数
def should_continue(state: MessagesState) -> Literal["tools", "end"]:
    """判断是否需要调用工具"""
    messages = state["messages"]
    last_message = messages[-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"

# 创建工具节点
tool_node = ToolNode(tools)

# 构建图
workflow = StateGraph(MessagesState)

# 添加节点
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# 设置入口点
workflow.set_entry_point("agent")

# 添加条件边
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": "__end__"
    }
)

# 从工具返回到 agent
workflow.add_edge("tools", "agent")

# 编译图
app = workflow.compile()

def chat(question: str, verbose: bool = True) -> str:
    """发送问题并获取回答"""
    try:
        if verbose:
            print(f"\n{'='*60}")
            print(f"问题: {question}")
            print(f"{'='*60}")
        
        result = app.invoke(
            {"messages": [HumanMessage(content=question)]},
            {"recursion_limit": 10}
        )
        
        # 获取最后一条消息
        final_message = result["messages"][-1]
        
        if verbose and len(result["messages"]) > 2:
            print(f"\n[Debug] 总共 {len(result['messages'])} 条消息")
        
        return final_message.content
    except Exception as e:
        return f"错误: {str(e)}"

if __name__ == "__main__":
    print("=" * 60)
    print("Anthropic 风格问答 Agent (LangGraph 版本)")
    print("=" * 60)
    
    # 测试问题
    test_questions = [
        "你好！请介绍一下你自己。",
        "Python 和 JavaScript 的主要区别是什么？",
        "帮我计算 123 + 456",
        "什么是机器学习？请简单解释。"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n\n{'#'*60}")
        print(f"测试 {i}/{len(test_questions)}")
        print(f"{'#'*60}")
        
        answer = chat(question, verbose=True)
        print(f"\n回答: {answer}")

