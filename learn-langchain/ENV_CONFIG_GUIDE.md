# 环境变量配置示例

请在项目根目录创建 `.env` 文件，并添加以下配置：

```bash
# =============================================================================
# Anthropic API 配置
# =============================================================================

# Anthropic API Key（必需）
# 获取方式：https://console.anthropic.com/
ANTHROPIC_API_KEY=sk-ant-xxxxx

# 自定义 API 端点（可选）
# 默认：https://api.anthropic.com
# 如果使用代理或第三方兼容服务，可以修改此项
# ANTHROPIC_BASE_URL=https://api.anthropic.com

# 模型名称（可选）
# 默认：claude-3-5-sonnet-20241022
# 可选值：
#   - claude-3-5-sonnet-20241022 (推荐，平衡性能和成本)
#   - claude-3-opus-20240229 (最强性能)
#   - claude-3-sonnet-20240229 (性价比高)
#   - claude-3-haiku-20240307 (最快速度，低成本)
# ANTHROPIC_MODEL_NAME=claude-3-5-sonnet-20241022

# =============================================================================
# OpenAI API 配置（用于其他示例）
# =============================================================================

# OpenAI 兼容的 API 配置
# API_KEY=your_api_key
# BASE_URL=https://api.openai.com/v1
# MODEL_NAME=gpt-4

# =============================================================================
# 其他服务配置
# =============================================================================

# OpenWeatherMap API Key（用于天气查询示例）
# OPENWEATHER_API_KEY=your_openweather_api_key
```

## 配置说明

### 1. ANTHROPIC_API_KEY（必需）

这是使用 Anthropic Claude 模型的必需参数。

**获取步骤：**
1. 访问 https://console.anthropic.com/
2. 注册并登录账号
3. 进入 API Keys 页面
4. 创建新的 API Key
5. 复制 Key（格式类似：`sk-ant-api03-...`）

### 2. ANTHROPIC_BASE_URL（可选）

自定义 API 端点地址，用于以下场景：

- **使用代理服务**：某些地区可能需要通过代理访问
  ```bash
  ANTHROPIC_BASE_URL=https://your-proxy-service.com/v1
  ```

- **使用第三方兼容服务**：一些服务提供 Anthropic 兼容的 API
  ```bash
  ANTHROPIC_BASE_URL=https://compatible-service.com/anthropic
  ```

- **默认值**：如果不设置，将使用官方地址 `https://api.anthropic.com`

### 3. ANTHROPIC_MODEL_NAME（可选）

指定要使用的 Claude 模型。

| 模型 | 特点 | 适用场景 |
|------|------|---------|
| `claude-3-5-sonnet-20241022` | 最新版本，性能强大 | **推荐使用**，适合大多数场景 |
| `claude-3-opus-20240229` | 最强性能，最贵 | 复杂推理、专业任务 |
| `claude-3-sonnet-20240229` | 平衡性能 | 日常对话、一般任务 |
| `claude-3-haiku-20240307` | 速度快，成本低 | 简单任务、高频调用 |

## 使用示例

创建好 `.env` 文件后，代码会自动读取配置：

```python
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

# 方式1：使用默认配置
model = ChatAnthropic(
    model=os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-5-sonnet-20241022"),
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 方式2：包含自定义 base_url
model_kwargs = {
    "model": os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-5-sonnet-20241022"),
    "api_key": os.getenv("ANTHROPIC_API_KEY"),
    "temperature": 0.7,
    "max_tokens": 2048
}

base_url = os.getenv("ANTHROPIC_BASE_URL")
if base_url:
    model_kwargs["base_url"] = base_url

model = ChatAnthropic(**model_kwargs)
```

## 安全提示

⚠️ **重要安全提示：**

1. **不要提交 `.env` 文件到 Git**
   - 确保 `.env` 在 `.gitignore` 中
   - API Key 是敏感信息，泄露可能导致费用损失

2. **定期更换 API Key**
   - 定期在控制台生成新的 Key
   - 删除不再使用的旧 Key

3. **设置使用限额**
   - 在 Anthropic Console 中设置每月预算
   - 监控 API 使用情况

4. **环境隔离**
   - 生产环境和开发环境使用不同的 Key
   - 团队成员使用各自的 Key

## 验证配置

运行以下命令验证配置是否正确：

```bash
python -c "
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('ANTHROPIC_API_KEY')
base_url = os.getenv('ANTHROPIC_BASE_URL')
model = os.getenv('ANTHROPIC_MODEL_NAME')

print(f'API Key: {'已设置' if key else '未设置'}')
print(f'Base URL: {base_url if base_url else '使用默认'}')
print(f'Model: {model if model else '使用默认 (claude-3-5-sonnet-20241022)'}')
"
```

## 常见问题

### Q: 如何判断配置是否生效？

运行任何一个示例文件，如果能正常返回结果，说明配置正确。

### Q: API Key 在哪里获取？

访问 https://console.anthropic.com/ 注册账号后，在 Settings > API Keys 页面创建。

### Q: 是否需要付费？

Anthropic 提供免费试用额度，超出后需要绑定支付方式。具体额度和价格请查看官方网站。

### Q: 代理服务推荐？

由于网络原因，某些地区可能需要使用代理。请自行寻找可靠的服务商，或者使用云服务器部署中转服务。

### Q: 如何查看 API 使用情况？

登录 Anthropic Console，在 Usage 页面可以查看详细的 API 调用统计和费用。

---

**更新日期**: 2026-02-10

