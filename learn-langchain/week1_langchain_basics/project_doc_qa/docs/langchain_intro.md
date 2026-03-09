# LangChain 简介

LangChain是一个用于开发由语言模型驱动的应用程序的框架。它提供了一套工具、组件和接口,简化了创建由大型语言模型(LLM)和聊天模型驱动的应用程序的过程。

## 核心概念

### 1. 组件(Components)

LangChain提供了标准的、可扩展的接口和外部集成,用于以下模块:

- **Model I/O**: 与语言模型的接口
- **Retrieval**: 与应用程序特定数据的接口  
- **Agents**: 让LLM根据高级指令选择要使用的工具

### 2. Chains

Chain允许我们将多个组件组合在一起以创建一个单一的、连贯的应用程序。例如,我们可以创建一个chain,它接收用户输入,使用Prompt模板对其进行格式化,然后将格式化的响应传递给LLM。

### 3. Agents

Agents使用LLM来决定采取什么行动。Agents可以访问一套工具,并根据用户输入决定调用哪个工具。

## 为什么使用LangChain?

1. **简化开发**: 提供标准化接口,减少重复代码
2. **灵活性**: 支持多种LLM提供商(OpenAI, Anthropic等)  
3. **可组合性**: 通过Chains和Agents组合功能
4. **生产就绪**: 包含监控、日志等工具

## 快速开始

```python
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
response = model.invoke([HumanMessage(content="你好!")])
print(response.content)
```

## 主要功能

### Prompt模板

Prompt模板帮助格式化用户输入:

```python
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的助手"),
    ("user", "{input}")
])
```

### 输出解析

输出解析器帮助结构化LLM的输出:

```python
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

parser = PydanticOutputParser(pydantic_object=Person)
```

### 记忆管理

LangChain提供多种方式来管理对话历史:

- ConversationBufferMemory: 存储所有对话
- ConversationSummaryMemory: 存储对话摘要
- ConversationBufferWindowMemory: 只保留最近N轮对话

## 应用场景

- 聊天机器人
- 问答系统
- 文档分析
- 代码生成
- 数据分析
- 自动化任务

## 学习资源

- 官方文档: https://python.langchain.com/
- GitHub: https://github.com/langchain-ai/langchain
- 社区: Discord, Twitter

## 总结

LangChain是一个强大的框架,它简化了LLM应用的开发。通过其模块化的设计,开发者可以快速构建复杂的AI应用程序。
