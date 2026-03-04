import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# 加载环境变量
load_dotenv()

@tool
def get_weather_wttr(location: str) -> str:
    """
    使用 wttr.in 获取天气信息（免费，无需API key）
    
    Args:
        location: 城市名称，如 "Beijing", "Tokyo", "New York"
    
    Returns:
        天气信息字符串
    """
    try:
        # wttr.in 格式说明:
        # %C - 天气状况
        # %t - 温度
        # %h - 湿度
        # %w - 风速
        # %p - 降水量
        url = f"https://wttr.in/{location}?format=%C+Temperature:+%t+Humidity:+%h+Wind:+%w"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            weather_info = response.text.strip()
            return f"Weather in {location}: {weather_info}"
        else:
            return f"Failed to fetch weather for {location}. Status code: {response.status_code}"
    
    except requests.exceptions.Timeout:
        return f"Request timeout when fetching weather for {location}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@tool
def get_weather_openweather(location: str) -> str:
    """
    使用 OpenWeatherMap API 获取天气信息
    需要在 .env 文件中配置: OPENWEATHER_API_KEY=your_api_key
    免费注册地址: https://openweathermap.org/api
    
    Args:
        location: 城市名称，如 "Beijing", "Tokyo", "New York"
    
    Returns:
        详细的天气信息
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        return "OpenWeatherMap API key not configured. Please add OPENWEATHER_API_KEY to your .env file."
    
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric",  # 使用摄氏度
            "lang": "zh_cn"     # 中文描述（如果需要英文，改为 "en"）
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # 提取关键信息
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            
            weather_report = f"""Weather Report for {location}:
- Condition: {description}
- Temperature: {temp}°C (feels like {feels_like}°C)
- Min/Max: {temp_min}°C / {temp_max}°C
- Humidity: {humidity}%
- Pressure: {pressure} hPa
- Wind Speed: {wind_speed} m/s"""
            
            return weather_report
        
        elif response.status_code == 401:
            return "Invalid API key. Please check your OPENWEATHER_API_KEY in .env file."
        elif response.status_code == 404:
            return f"Location '{location}' not found. Please check the city name."
        else:
            return f"Failed to fetch weather. Status code: {response.status_code}, Message: {response.text}"
    
    except requests.exceptions.Timeout:
        return f"Request timeout when fetching weather for {location}"
    except requests.exceptions.RequestException as e:
        return f"Network error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@tool  
def get_weather_weatherapi(location: str) -> str:
    """
    使用 WeatherAPI.com 获取天气信息
    需要在 .env 文件中配置: WEATHERAPI_KEY=your_api_key
    免费注册地址: https://www.weatherapi.com/
    
    Args:
        location: 城市名称，如 "Beijing", "Tokyo", "New York"
    
    Returns:
        详细的天气信息
    """
    api_key = os.getenv("WEATHERAPI_KEY")
    
    if not api_key:
        return "WeatherAPI key not configured. Please add WEATHERAPI_KEY to your .env file."
    
    try:
        url = f"http://api.weatherapi.com/v1/current.json"
        params = {
            "key": api_key,
            "q": location,
            "aqi": "no"  # 不需要空气质量数据
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            location_info = data["location"]
            current = data["current"]
            
            weather_report = f"""Weather Report for {location_info['name']}, {location_info['country']}:
- Condition: {current['condition']['text']}
- Temperature: {current['temp_c']}°C (feels like {current['feelslike_c']}°C)
- Humidity: {current['humidity']}%
- Wind Speed: {current['wind_kph']} km/h
- Wind Direction: {current['wind_dir']}
- Pressure: {current['pressure_mb']} mb
- UV Index: {current['uv']}
- Last Updated: {current['last_updated']}"""
            
            return weather_report
        
        else:
            error_data = response.json()
            return f"Error: {error_data.get('error', {}).get('message', 'Unknown error')}"
    
    except requests.exceptions.Timeout:
        return f"Request timeout when fetching weather for {location}"
    except requests.exceptions.RequestException as e:
        return f"Network error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


# 创建模型实例
model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# 创建agent，可以选择使用不同的天气工具
# 选项1: 使用免费的 wttr.in (推荐，无需配置)
agent = create_agent(model, tools=[get_weather_wttr])

# 选项2: 使用 OpenWeatherMap (需要配置 API key)
# agent = create_agent(model, tools=[get_weather_openweather])

# 选项3: 使用 WeatherAPI.com (需要配置 API key)
# agent = create_agent(model, tools=[get_weather_weatherapi])

# 选项4: 提供多个工具让 agent 选择
# agent = create_agent(model, tools=[get_weather_wttr, get_weather_openweather, get_weather_weatherapi])


if __name__ == "__main__":
    # 测试天气查询
    print("=" * 60)
    print("Testing Weather Agent with Real API")
    print("=" * 60)
    
    # 示例1: 查询北京天气
    result = agent.invoke({
        "messages": [{"role": "user", "content": "What is the weather in Beijing?"}]
    })
    print("\n📍 Beijing Weather:")
    print(result["messages"][-1].content)
    
    print("\n" + "=" * 60)
    
    # 示例2: 查询多个城市
    result = agent.invoke({
        "messages": [{"role": "user", "content": "Compare the weather in Tokyo, London, and New York"}]
    })
    print("\n🌍 Multiple Cities Comparison:")
    print(result["messages"][-1].content)
    
    print("\n" + "=" * 60)

