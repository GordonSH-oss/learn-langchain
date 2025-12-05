import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# 加载环境变量
load_dotenv()

@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"The weather in {location} is sunny."

model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

agent = create_agent(model, tools=[get_weather])

# ✅ 正确
result = agent.invoke({
    "messages": [{"role": "user", "content": "What is the weather in Tokyo?"}]
})

print(result["messages"][-1].content)