# Anthropic Agent 快速开始 🚀

在 3 分钟内开始使用 Anthropic Claude 模型进行问答！

## 快速开始（3 步）

### 步骤 1: 安装依赖

```bash
pip install langchain langchain-anthropic python-dotenv
```

### 步骤 2: 配置 API Key

在项目根目录创建 `.env` 文件：

```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

> 💡 **获取 API Key**: 访问 [Anthropic Console](https://console.anthropic.com/) 注册并创建 API Key

### 步骤 3: 运行示例

```bash
# 运行测试（推荐先运行此文件检查配置）
python test-anthropic-agent.py

# 运行简单问答示例（推荐新手）
python use-agent-anthropic-qa-only.py

# 运行带工具的 Agent 示例
python use-agent-anthropic-simple.py
```

## 📁 文件说明

| 文件名 | 说明 | 推荐度 |
|-------|------|--------|
| `test-anthropic-agent.py` | 测试配置和基本功能 | ⭐⭐⭐ |
| `use-agent-anthropic-qa-only.py` | 简单问答（无框架） | ⭐⭐⭐ 推荐新手 |
| `use-agent-anthropic-simple.py` | Agent 框架（带工具） | ⭐⭐ 适合进阶 |
| `ANTHROPIC_AGENT_README.md` | 完整使用文档 | 📖 详细说明 |
| `ENV_CONFIG_GUIDE.md` | 环境配置指南 | 📖 配置参考 |

## 🎯 使用示例

### 示例 1: 最简单的问答

```python
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

load_dotenv()

# 初始化模型
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 提问
response = model.invoke([HumanMessage(content="什么是 Python？")])
print(response.content)
```

### 示例 2: 带上下文的对话

```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

messages = [
    SystemMessage(content="你是一个友好的助手"),
    HumanMessage(content="我想学习编程"),
    AIMessage(content="太好了！你想学习哪种编程语言？"),
    HumanMessage(content="Python")
]

response = model.invoke(messages)
print(response.content)
```

### 示例 3: 流式输出

```python
for chunk in model.stream([HumanMessage(content="数到 10")]):
    print(chunk.content, end="", flush=True)
```

## ⚙️ 可选配置

在 `.env` 文件中添加可选配置：

```bash
# 使用自定义端点（代理或第三方服务）
ANTHROPIC_BASE_URL=https://your-proxy.com/v1

# 指定模型版本
ANTHROPIC_MODEL_NAME=claude-3-haiku-20240307
```

## 🔧 支持的模型

| 模型 | 速度 | 性能 | 成本 | 适用场景 |
|------|-----|------|------|---------|
| `claude-3-5-sonnet-20241022` | ⚡⚡⚡ | 🎯🎯🎯🎯 | 💰💰 | **推荐**，日常使用 |
| `claude-3-opus-20240229` | ⚡⚡ | 🎯🎯🎯🎯🎯 | 💰💰💰 | 复杂任务 |
| `claude-3-haiku-20240307` | ⚡⚡⚡⚡ | 🎯🎯🎯 | 💰 | 简单任务，高频调用 |

## 🐛 故障排查

### 问题 1: `ModuleNotFoundError: No module named 'langchain_anthropic'`

**解决方案:**
```bash
pip install langchain-anthropic
```

### 问题 2: API Key 错误

**解决方案:**
1. 检查 `.env` 文件是否在项目根目录
2. 确认 `ANTHROPIC_API_KEY` 格式正确（以 `sk-ant-` 开头）
3. 运行测试文件验证：
   ```bash
   python test-anthropic-agent.py
   ```

### 问题 3: 网络连接超时

**解决方案:**
```bash
# 在 .env 中添加代理地址
ANTHROPIC_BASE_URL=https://your-proxy-service.com/v1
```

或者在代码中设置超时时间：
```python
model = ChatAnthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    timeout=60,  # 60 秒超时
    max_retries=3
)
```

## 📚 进阶学习

1. **阅读完整文档**: `ANTHROPIC_AGENT_README.md`
2. **学习配置选项**: `ENV_CONFIG_GUIDE.md`
3. **查看其他示例**: 项目中的其他 `use-agent-*.py` 文件

## 💡 最佳实践

1. **先运行测试**: 确保配置正确
   ```bash
   python test-anthropic-agent.py
   ```

2. **从简单开始**: 先用 `use-agent-anthropic-qa-only.py`

3. **控制成本**: 
   - 开发时使用 `claude-3-haiku-20240307`（更便宜）
   - 生产时使用 `claude-3-5-sonnet-20241022`（更好）

4. **监控使用**: 定期检查 [Anthropic Console](https://console.anthropic.com/) 的使用情况

## 🆘 获取帮助

- **Anthropic 官方文档**: https://docs.anthropic.com/
- **LangChain 文档**: https://python.langchain.com/docs/integrations/chat/anthropic
- **项目 Issues**: 如果遇到问题，欢迎提 Issue

## 📊 性能对比

运行以下命令对比不同模型的性能：

```bash
# 对比响应速度（需要先设置好 API Key）
python -c "
from time import time
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

models = [
    'claude-3-5-sonnet-20241022',
    'claude-3-haiku-20240307'
]

for model_name in models:
    model = ChatAnthropic(model=model_name, api_key=os.getenv('ANTHROPIC_API_KEY'))
    start = time()
    model.invoke([HumanMessage(content='Hello')])
    print(f'{model_name}: {time()-start:.2f}s')
"
```

## 🎉 开始使用

现在你已经准备好了！运行：

```bash
python test-anthropic-agent.py
```

如果看到所有测试通过，恭喜你配置成功！🎊

---

**最后更新**: 2026-02-10  
**维护者**: 你的团队

