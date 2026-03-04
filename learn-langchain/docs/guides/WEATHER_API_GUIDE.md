# 使用真实天气API的Agent示例

本示例展示了如何在 LangChain Agent 中集成真实的天气API接口。

## 📋 支持的天气API

### 1. wttr.in (推荐 ⭐)
- **优点**: 完全免费，无需注册，无需API key
- **缺点**: 功能相对简单
- **使用**: 直接可用，无需配置

### 2. OpenWeatherMap
- **优点**: 功能丰富，数据准确
- **免费额度**: 1,000次调用/天
- **注册地址**: https://openweathermap.org/api
- **配置**: 在 `.env` 文件中添加 `OPENWEATHER_API_KEY=your_key`

### 3. WeatherAPI.com
- **优点**: 免费额度最高，数据详细
- **免费额度**: 1,000,000次调用/月
- **注册地址**: https://www.weatherapi.com/
- **配置**: 在 `.env` 文件中添加 `WEATHERAPI_KEY=your_key`

## 🚀 快速开始

### 方式1: 使用免费的 wttr.in (无需配置)

```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from use_agent_tool_real_weather import get_weather_wttr

model = ChatOpenAI(...)
agent = create_agent(model, tools=[get_weather_wttr])

result = agent.invoke({
    "messages": [{"role": "user", "content": "What is the weather in Tokyo?"}]
})
print(result["messages"][-1].content)
```

### 方式2: 使用 OpenWeatherMap (需要API key)

1. 注册并获取API key: https://openweathermap.org/api
2. 在 `.env` 文件中添加: `OPENWEATHER_API_KEY=your_api_key`
3. 修改代码:

```python
from use_agent_tool_real_weather import get_weather_openweather

agent = create_agent(model, tools=[get_weather_openweather])
```

### 方式3: 使用多个天气源 (让Agent自动选择)

```python
from use_agent_tool_real_weather import (
    get_weather_wttr, 
    get_weather_openweather, 
    get_weather_weatherapi
)

agent = create_agent(model, tools=[
    get_weather_wttr,
    get_weather_openweather,
    get_weather_weatherapi
])
```

## 📦 安装依赖

```bash
pip install requests langchain langchain-openai python-dotenv
```

## 🔧 环境变量配置

在项目根目录创建 `.env` 文件：

```env
# LangChain 配置
MODEL_NAME=gpt-4
BASE_URL=https://api.openai.com/v1
API_KEY=your_openai_api_key

# 天气API配置（可选）
OPENWEATHER_API_KEY=your_openweather_api_key
WEATHERAPI_KEY=your_weatherapi_key
```

## 🧪 运行示例

```bash
# 运行完整示例
python use-agent-tool-real-weather.py

# 运行简化版本
python use-agent-tool.py
```

## 📝 原始代码修改说明

原始的 `get_weather()` 函数只是返回硬编码的字符串：

```python
@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"The weather in {location} is sunny."
```

修改后的版本会调用真实的天气API：

```python
@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    try:
        url = f"https://wttr.in/{location}?format=%C+%t+%h+%w"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Weather in {location}: {response.text.strip()}"
    except Exception as e:
        return f"Error: {str(e)}"
```

## 🌟 主要改进

1. **真实数据**: 调用实际的天气API获取真实天气信息
2. **错误处理**: 添加完善的异常处理机制
3. **多种选择**: 提供多个天气API供选择
4. **免费方案**: wttr.in 完全免费，无需注册
5. **详细信息**: 返回温度、湿度、风速等详细数据

## ⚠️ 注意事项

1. **API限制**: 注意免费API的调用次数限制
2. **超时设置**: 设置合理的请求超时时间
3. **错误处理**: 处理网络错误、API错误等异常情况
4. **位置名称**: 使用英文城市名称，如 "Beijing" 而不是 "北京"

## 🔍 API响应示例

### wttr.in 响应:
```
Partly cloudy Temperature: +15°C Humidity: 60% Wind: 10km/h
```

### OpenWeatherMap 响应:
```json
{
  "main": {
    "temp": 15.2,
    "feels_like": 14.8,
    "humidity": 60
  },
  "weather": [
    {"description": "partly cloudy"}
  ],
  "wind": {
    "speed": 2.8
  }
}
```

## 📚 相关资源

- [wttr.in GitHub](https://github.com/chubin/wttr.in)
- [OpenWeatherMap 文档](https://openweathermap.org/api)
- [WeatherAPI 文档](https://www.weatherapi.com/docs/)
- [LangChain Tools 文档](https://python.langchain.com/docs/modules/tools/)

