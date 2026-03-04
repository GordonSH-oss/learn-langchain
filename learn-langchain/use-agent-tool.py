import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# 加载环境变量
load_dotenv()

@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    
    # 方法1: 使用 wttr.in (免费，无需API key)
    try:
        url = f"https://wttr.in/{location}?format=%C+%t+%h+%w"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Weather in {location}: {response.text.strip()}"
    except Exception as e:
        pass
    
    # 方法2: 使用 OpenWeatherMap API (需要注册获取免费API key)
    # 在 .env 文件中添加: OPENWEATHER_API_KEY=your_api_key
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if api_key:
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": location,
                "appid": api_key,
                "units": "metric",  # 使用摄氏度
                "lang": "zh_cn"     # 中文描述
            }
            response = requests.get(url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                return f"Weather in {location}: {desc}, Temperature: {temp}°C, Humidity: {humidity}%, Wind Speed: {wind_speed}m/s"
        except Exception as e:
            return f"Error fetching weather data: {str(e)}"
    
    return f"Unable to fetch weather data for {location}. Please check the location name or API configuration."

model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

agent = create_agent(model, tools=[get_weather])

# ✅ 正确
result = agent.invoke({
    "messages": [{"role": "user", "content": "What is the weather in Beijing?"}]
})

print(result["messages"][-1].content)