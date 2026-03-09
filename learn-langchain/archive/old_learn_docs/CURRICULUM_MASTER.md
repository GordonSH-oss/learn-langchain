# LangChain & LangGraph 精通计划（60天）

> 从零基础到精通 LangChain、LangGraph 和 DeepAgents 的完整学习路径

## 🎯 课程目标

完成本课程后，你将能够：

1. ✅ **LangChain 核心掌握** - 深入理解 LangChain 的所有核心概念
2. ✅ **LangGraph 精通** - 能够构建复杂的状态机和工作流
3. ✅ **DeepAgents 应用** - 使用 DeepAgents 构建高级 AI 应用
4. ✅ **生产级开发** - 能够开发、部署和维护生产级 AI 应用
5. ✅ **架构设计** - 能够设计复杂的 AI 系统架构

## 📊 课程结构

```
第一阶段（Week 1-2）：LangChain 基础
  ├── LLM 调用和消息管理
  ├── Prompt 工程
  ├── Chain 和 LCEL
  └── 输出解析器

第二阶段（Week 3-4）：Agent 基础
  ├── Tools 工具系统
  ├── Agent 创建和配置
  ├── 记忆管理
  └── 实战项目

第三阶段（Week 5-6）：LangGraph 核心
  ├── StateGraph 原理
  ├── 条件路由和循环
  ├── 检查点和持久化
  └── 高级模式

第四阶段（Week 7-8）：DeepAgents 和生产实践
  ├── DeepAgents 架构
  ├── 多 Agent 系统
  ├── 性能优化
  └── 部署和监控
```

## 📅 详细学习计划

---

## 🔰 第一阶段：LangChain 基础（Week 1-2，Day 1-14）

### Week 1：核心概念和基础应用

#### Day 1：环境搭建和第一个应用

**学习目标**：
- 理解 LangChain 生态系统
- 配置开发环境
- 运行第一个 LLM 应用

**学习内容**：
1. LangChain 是什么，为什么需要它
2. LangChain vs 直接调用 LLM API 的区别
3. 安装和配置（virtualenvwrapper 环境）
4. 理解 LLM、Prompt、Message 的概念

**实践任务**：
```bash
# 创建虚拟环境
mkvirtualenv -p python3.12 langchain-master

# 安装依赖
pip install langchain langchain-anthropic langchain-openai langgraph python-dotenv

# 配置 API Keys
cd learn-langchain
cp .env.example .env
# 编辑 .env，填入 ANTHROPIC_API_KEY

# 运行第一个示例
python examples/use-agent-anthropic-qa-only.py
```

**理论学习**：
- 阅读 LangChain 官方文档概览
- 理解模型、提示词、输出的流程
- 了解不同的 LLM 提供商

**作业**：
创建一个简单的对话程序，能够：
- 接收用户输入
- 调用 LLM 生成回复
- 显示结果

**参考文档**：
- `docs/guides/ENV_CONFIG_GUIDE.md`
- `ANTHROPIC_AGENT_README.md`

---

#### Day 2：消息系统和对话管理

**学习目标**：
- 掌握 LangChain 的消息类型
- 理解对话历史的管理
- 实现多轮对话

**学习内容**：
1. 消息类型详解：
   - `HumanMessage` - 用户消息
   - `AIMessage` - AI 回复
   - `SystemMessage` - 系统提示词
   - `FunctionMessage` - 函数调用结果
   - `ToolMessage` - 工具调用结果

2. 对话历史的结构
3. 上下文窗口管理

**实践任务**：
```python
# 文件：projects/day02_chat_with_history.py

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()

# 初始化模型
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创建对话历史
history = InMemoryChatMessageHistory()
history.add_message(SystemMessage(content="你是一个 Python 编程专家"))

def chat(user_input: str) -> str:
    """发送消息并获取回复"""
    # 添加用户消息
    history.add_message(HumanMessage(content=user_input))
    
    # 获取所有消息
    messages = history.messages
    
    # 调用模型
    response = model.invoke(messages)
    
    # 保存 AI 回复
    history.add_message(AIMessage(content=response.content))
    
    return response.content

# 测试对话
if __name__ == "__main__":
    print("对话开始（输入 'quit' 退出）\n")
    
    while True:
        user_input = input("你: ")
        if user_input.lower() in ['quit', 'exit', '退出']:
            break
        
        response = chat(user_input)
        print(f"AI: {response}\n")
```

**深入研究**：
- 消息的 token 计算
- 上下文窗口限制的处理
- 对话历史的压缩策略

**作业**：
实现一个支持以下功能的对话系统：
1. 多轮对话
2. 显示对话历史
3. 清空历史的命令
4. 保存对话到文件

---

#### Day 3：Prompt 工程基础

**学习目标**：
- 掌握 Prompt 设计原则
- 学习 Few-shot Learning
- 使用 PromptTemplate

**学习内容**：
1. Prompt 工程基础：
   - 清晰的指令
   - 上下文提供
   - 输出格式指定
   - Few-shot 示例

2. PromptTemplate 使用：
   - 字符串模板
   - f-string 模板
   - Jinja2 模板

3. ChatPromptTemplate：
   - 消息列表模板
   - 系统消息 + 用户消息
   - 动态内容插入

**实践任务**：
```python
# 文件：projects/day03_prompt_engineering.py

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 示例 1：代码生成 Prompt
code_gen_prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个 Python 专家。请按照以下要求生成代码：
1. 代码要清晰易读
2. 添加详细的注释
3. 包含错误处理
4. 遵循 PEP 8 规范"""),
    ("human", "请帮我写一个函数：{requirement}")
])

# 示例 2：Few-shot Learning
translation_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的翻译助手"),
    ("human", "技术文档 -> Technical Documentation"),
    ("ai", "好的，我理解了专业术语的翻译风格"),
    ("human", "人工智能 -> Artificial Intelligence"),
    ("ai", "理解，我会保持准确的技术翻译"),
    ("human", "{text}")
])

# 示例 3：带历史的对话
conversation_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的助手，会记住之前的对话内容"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 测试
if __name__ == "__main__":
    # 测试代码生成
    chain = code_gen_prompt | model
    result = chain.invoke({"requirement": "读取 JSON 文件并解析内容"})
    print("=== 代码生成 ===")
    print(result.content)
    print()
    
    # 测试翻译
    chain = translation_prompt | model
    result = chain.invoke({"text": "深度学习"})
    print("=== 翻译 ===")
    print(result.content)
```

**深入研究**：
- 不同任务的 Prompt 模式
- Prompt 优化技巧
- Chain of Thought (CoT)
- ReAct Prompting

**作业**：
设计以下场景的 Prompt：
1. 代码审查助手
2. 文档摘要生成器
3. 技术问答机器人
4. 测试用例生成器

---

#### Day 4：Chain 和 LCEL（LangChain Expression Language）

**学习目标**：
- 理解 Chain 的概念
- 掌握 LCEL 语法
- 构建复杂的处理链

**学习内容**：
1. Chain 基础：
   - 什么是 Chain
   - Sequential Chain
   - Parallel Chain
   - Router Chain

2. LCEL（LangChain Expression Language）：
   - 管道操作符 `|`
   - Runnable 接口
   - RunnablePassthrough
   - RunnableLambda

3. Chain 组合模式：
   - 串行处理
   - 并行处理
   - 条件分支
   - 循环处理

**实践任务**：
```python
# 文件：projects/day04_chains_and_lcel.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_anthropic import ChatAnthropic
from operator import itemgetter
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# === 示例 1：简单的 Chain ===
prompt = ChatPromptTemplate.from_template("讲一个关于{topic}的笑话")
chain = prompt | model | StrOutputParser()

result = chain.invoke({"topic": "程序员"})
print("=== 简单 Chain ===")
print(result)
print()

# === 示例 2：多步骤 Chain ===
# 步骤 1：生成故事大纲
outline_prompt = ChatPromptTemplate.from_template(
    "为{topic}主题生成一个故事大纲（3-5个要点）"
)

# 步骤 2：根据大纲写故事
story_prompt = ChatPromptTemplate.from_template(
    "根据以下大纲，写一个详细的故事：\n{outline}"
)

# 组合 Chain
multi_chain = (
    {"outline": outline_prompt | model | StrOutputParser()}
    | story_prompt
    | model
    | StrOutputParser()
)

result = multi_chain.invoke({"topic": "AI 觉醒"})
print("=== 多步骤 Chain ===")
print(result)
print()

# === 示例 3：并行 Chain ===
from langchain_core.runnables import RunnableParallel

# 同时生成标题、摘要和标签
parallel_chain = RunnableParallel(
    title=ChatPromptTemplate.from_template("为以下内容生成标题：{content}") | model | StrOutputParser(),
    summary=ChatPromptTemplate.from_template("为以下内容生成摘要：{content}") | model | StrOutputParser(),
    tags=ChatPromptTemplate.from_template("为以下内容生成5个标签：{content}") | model | StrOutputParser()
)

result = parallel_chain.invoke({
    "content": "LangChain 是一个用于开发由语言模型驱动的应用程序的框架"
})
print("=== 并行 Chain ===")
print(f"标题: {result['title']}")
print(f"摘要: {result['summary']}")
print(f"标签: {result['tags']}")
print()

# === 示例 4：使用 RunnableLambda 自定义处理 ===
def uppercase_output(text: str) -> str:
    """将输出转为大写"""
    return text.upper()

def add_prefix(text: str) -> str:
    """添加前缀"""
    return f"[AI Generated] {text}"

custom_chain = (
    prompt
    | model
    | StrOutputParser()
    | RunnableLambda(uppercase_output)
    | RunnableLambda(add_prefix)
)

result = custom_chain.invoke({"topic": "Python"})
print("=== 自定义处理 Chain ===")
print(result)
```

**深入研究**：
- Chain 的错误处理
- Chain 的流式输出
- Chain 的缓存机制
- Chain 的性能优化

**作业**：
构建一个文章处理 Pipeline：
1. 输入：原始文章
2. 步骤 1：生成标题
3. 步骤 2：提取关键词
4. 步骤 3：生成摘要
5. 步骤 4：翻译成英文
6. 输出：包含所有信息的结构化数据

---

#### Day 5：输出解析器（Output Parsers）

**学习目标**：
- 理解输出解析器的作用
- 掌握不同类型的解析器
- 实现结构化输出

**学习内容**：
1. 为什么需要输出解析器
2. 常用解析器类型：
   - StrOutputParser
   - JsonOutputParser
   - PydanticOutputParser
   - ListOutputParser
   - DatetimeOutputParser
   - EnumOutputParser

3. 结构化输出：
   - 使用 Pydantic 模型
   - JSON Schema
   - 自动格式化 Prompt

**实践任务**：
```python
# 文件：projects/day05_output_parsers.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser,
    PydanticOutputParser,
)
from langchain_anthropic import ChatAnthropic
from pydantic import BaseModel, Field
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# === 示例 1：JsonOutputParser ===
json_parser = JsonOutputParser()

json_prompt = ChatPromptTemplate.from_template(
    """提取以下文本的关键信息，以 JSON 格式返回：
    
文本：{text}

请返回以下格式的 JSON：
{{
    "title": "标题",
    "author": "作者",
    "date": "日期",
    "summary": "摘要"
}}
"""
)

json_chain = json_prompt | model | json_parser

result = json_chain.invoke({
    "text": "《深度学习》是由 Ian Goodfellow 于 2016 年出版的经典教材。"
})
print("=== JSON 解析器 ===")
print(result)
print()

# === 示例 2：PydanticOutputParser ===
class Article(BaseModel):
    """文章信息"""
    title: str = Field(description="文章标题")
    author: str = Field(description="作者名")
    published_date: str = Field(description="发布日期")
    tags: List[str] = Field(description="文章标签")
    summary: str = Field(description="文章摘要")
    category: str = Field(description="文章分类")

pydantic_parser = PydanticOutputParser(pydantic_object=Article)

pydantic_prompt = ChatPromptTemplate.from_template(
    """分析以下文章并提取信息：

{text}

{format_instructions}
"""
)

pydantic_chain = pydantic_prompt | model | pydantic_parser

result = pydantic_chain.invoke({
    "text": """
    标题：LangChain 入门教程
    作者：张三
    发布时间：2024-01-15
    
    这是一篇介绍 LangChain 框架的入门教程，涵盖了基本概念、安装配置和简单示例。
    主要面向 Python 开发者，特别是对 AI 应用感兴趣的工程师。
    """,
    "format_instructions": pydantic_parser.get_format_instructions()
})

print("=== Pydantic 解析器 ===")
print(f"标题: {result.title}")
print(f"作者: {result.author}")
print(f"日期: {result.published_date}")
print(f"标签: {result.tags}")
print(f"摘要: {result.summary}")
print(f"分类: {result.category}")
print()

# === 示例 3：复杂的结构化输出 ===
class CodeReview(BaseModel):
    """代码审查结果"""
    overall_quality: int = Field(description="代码整体质量评分（1-10）", ge=1, le=10)
    issues: List[str] = Field(description="发现的问题列表")
    suggestions: List[str] = Field(description="改进建议列表")
    good_practices: List[str] = Field(description="良好实践列表")
    complexity: str = Field(description="代码复杂度（low/medium/high）")
    
review_parser = PydanticOutputParser(pydantic_object=CodeReview)

review_prompt = ChatPromptTemplate.from_template(
    """请审查以下代码：

```python
{code}
```

{format_instructions}
"""
)

review_chain = review_prompt | model | review_parser

code_to_review = """
def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] > 0:
            result.append(data[i] * 2)
    return result
"""

result = review_chain.invoke({
    "code": code_to_review,
    "format_instructions": review_parser.get_format_instructions()
})

print("=== 代码审查 ===")
print(f"质量评分: {result.overall_quality}/10")
print(f"问题: {result.issues}")
print(f"建议: {result.suggestions}")
print(f"良好实践: {result.good_practices}")
print(f"复杂度: {result.complexity}")
```

**深入研究**：
- 输出验证和重试机制
- 处理解析错误
- 自定义输出解析器
- 流式输出的解析

**作业**：
创建一个简历解析器：
1. 输入：简历文本
2. 解析出：
   - 个人信息（姓名、联系方式）
   - 教育背景（学校、专业、时间）
   - 工作经历（公司、职位、时间、职责）
   - 技能列表
   - 项目经验
3. 输出：结构化的 Pydantic 对象

---

#### Day 6：Retrieval（检索）基础

**学习目标**：
- 理解 RAG（检索增强生成）
- 学习文档加载和分割
- 实现简单的检索系统

**学习内容**：
1. RAG 基础概念：
   - 为什么需要 RAG
   - RAG 的工作流程
   - 向量化和相似度搜索

2. 文档处理：
   - DocumentLoader
   - TextSplitter
   - 文档元数据

3. 向量存储：
   - VectorStore 概念
   - 常见向量数据库
   - 相似度搜索

**实践任务**：
```python
# 文件：projects/day06_retrieval_basics.py

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv

load_dotenv()

# === 示例 1：文档加载和分割 ===
# 创建示例文档
with open("sample_doc.txt", "w", encoding="utf-8") as f:
    f.write("""
LangChain 是一个用于开发由语言模型驱动的应用程序的框架。

核心概念包括：
1. Models: 语言模型接口
2. Prompts: 提示词模板
3. Chains: 将组件链接在一起
4. Agents: 使用语言模型进行决策
5. Memory: 在调用之间保持状态

LangChain 提供了许多实用功能，使得开发 LLM 应用变得更加简单和高效。
它支持多种 LLM 提供商，包括 OpenAI、Anthropic、Google 等。
    """)

# 加载文档
loader = TextLoader("sample_doc.txt", encoding="utf-8")
documents = loader.load()

print("=== 文档加载 ===")
print(f"文档数量: {len(documents)}")
print(f"文档内容预览: {documents[0].page_content[:100]}...")
print()

# 分割文档
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)

splits = text_splitter.split_documents(documents)
print("=== 文档分割 ===")
print(f"分块数量: {len(splits)}")
for i, split in enumerate(splits):
    print(f"\n块 {i+1}:")
    print(split.page_content)
print()

# === 示例 2：创建向量存储 ===
# 注意：这里需要 OpenAI API Key 用于 embeddings
# 也可以使用其他 embedding 模型

embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
vectorstore = FAISS.from_documents(splits, embeddings)

print("=== 向量存储创建完成 ===")
print()

# === 示例 3：检索 ===
query = "LangChain 的核心概念是什么？"
relevant_docs = vectorstore.similarity_search(query, k=2)

print(f"=== 检索查询：{query} ===")
for i, doc in enumerate(relevant_docs):
    print(f"\n相关文档 {i+1}:")
    print(doc.page_content)
print()

# === 示例 4：RAG Chain ===
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创建检索器
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 创建 RAG prompt
rag_prompt = ChatPromptTemplate.from_template("""
基于以下上下文回答问题：

上下文：
{context}

问题：{question}

请用中文回答，如果上下文中没有相关信息，请说"我不知道"。
""")

def format_docs(docs):
    """格式化文档"""
    return "\n\n".join(doc.page_content for doc in docs)

# 构建 RAG Chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | model
    | StrOutputParser()
)

# 测试
questions = [
    "LangChain 的核心概念有哪些？",
    "LangChain 支持哪些 LLM 提供商？",
    "什么是 Agents？"
]

print("=== RAG 问答 ===")
for question in questions:
    answer = rag_chain.invoke(question)
    print(f"\nQ: {question}")
    print(f"A: {answer}")

# 清理
os.remove("sample_doc.txt")
```

**深入研究**：
- 不同的 TextSplitter 策略
- Embedding 模型的选择
- 向量数据库的对比
- 检索优化技巧

**作业**：
构建一个文档问答系统：
1. 加载多个文档（至少 3 个）
2. 分割并向量化
3. 实现问答功能
4. 添加引用来源显示

---

#### Day 7：Week 1 项目 - 智能文档助手

**项目目标**：
综合 Week 1 所学知识，构建一个完整的智能文档助手

**功能需求**：
1. **文档管理**：
   - 支持加载多种格式（txt, md, pdf）
   - 文档分割和索引
   - 文档列表和预览

2. **智能问答**：
   - 基于文档内容回答问题
   - 显示答案来源
   - 支持多轮对话

3. **摘要生成**：
   - 为文档生成摘要
   - 提取关键词
   - 生成标题

4. **用户界面**：
   - 命令行交互
   - 清晰的提示和反馈
   - 错误处理

**项目结构**：
```
projects/week1_doc_assistant/
├── main.py              # 主程序入口
├── document_loader.py   # 文档加载器
├── rag_system.py        # RAG 系统
├── ui.py                # 用户界面
├── config.py            # 配置文件
└── docs/                # 测试文档目录
```

**实现要点**：
```python
# 文件：projects/week1_doc_assistant/main.py

"""
智能文档助手

功能：
1. 加载和管理文档
2. 基于文档的问答
3. 文档摘要生成
"""

from document_loader import DocumentManager
from rag_system import RAGSystem
from ui import UserInterface
import os
from dotenv import load_dotenv

load_dotenv()

class DocumentAssistant:
    """智能文档助手主类"""
    
    def __init__(self):
        self.doc_manager = DocumentManager()
        self.rag_system = RAGSystem(
            anthropic_key=os.getenv("ANTHROPIC_API_KEY"),
            openai_key=os.getenv("OPENAI_API_KEY")
        )
        self.ui = UserInterface()
    
    def run(self):
        """运行助手"""
        self.ui.show_welcome()
        
        while True:
            command = self.ui.get_command()
            
            if command == "quit":
                break
            elif command == "load":
                self.load_documents()
            elif command == "ask":
                self.ask_question()
            elif command == "summarize":
                self.summarize_document()
            elif command == "list":
                self.list_documents()
            elif command == "help":
                self.ui.show_help()
            else:
                self.ui.show_error("未知命令")
    
    def load_documents(self):
        """加载文档"""
        # 实现文档加载逻辑
        pass
    
    def ask_question(self):
        """回答问题"""
        # 实现问答逻辑
        pass
    
    def summarize_document(self):
        """生成摘要"""
        # 实现摘要生成逻辑
        pass
    
    def list_documents(self):
        """列出所有文档"""
        # 实现文档列表显示
        pass

if __name__ == "__main__":
    assistant = DocumentAssistant()
    assistant.run()
```

**评估标准**：
- ✅ 代码结构清晰
- ✅ 功能完整可用
- ✅ 错误处理完善
- ✅ 用户体验良好
- ✅ 代码有注释和文档

---

### Week 2：高级特性和记忆系统

#### Day 8-14：详见补充文档

由于内容较多，Week 2-8 的详细内容请参考：
- `CURRICULUM_WEEK2.md` - Agent 和 Tools
- `CURRICULUM_WEEK3-4.md` - LangGraph 深入
- `CURRICULUM_WEEK5-6.md` - DeepAgents
- `CURRICULUM_WEEK7-8.md` - 生产实践

---

## 📚 补充资源

### 官方文档
- [LangChain 官方文档](https://python.langchain.com/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
- [DeepAgents GitHub](https://github.com/deepagents/deepagents)

### 推荐阅读
- LangChain Cookbook
- LangGraph Examples
- AI Engineering 博客

### 社区资源
- LangChain Discord
- GitHub Discussions
- Stack Overflow

---

## 🎓 学习建议

1. **循序渐进**：不要跳过基础内容
2. **动手实践**：每天都要写代码
3. **记录笔记**：整理学习心得
4. **提出问题**：不懂就问，积极讨论
5. **构建项目**：学以致用，做实际项目
6. **阅读源码**：理解框架的实现原理

---

## 📝 作业提交

每周末提交本周作业：
- 代码文件
- README 说明
- 遇到的问题和解决方案
- 学习心得

---

**开始你的 LangChain 精通之旅！** 🚀
