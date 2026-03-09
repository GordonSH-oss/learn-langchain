# 实战项目：Docusaurus 文档智能问答助手

> 构建一个能够理解和问答 Docusaurus 文档站点的 AI 助手

## 🎯 项目目标

构建一个完整的文档问答系统，能够：
1. 自动爬取 Docusaurus 网站的 Markdown/MDX 文档
2. 对文档进行智能分割和向量化索引
3. 提供准确的问答能力
4. 引用文档来源

**难度**：⭐⭐⭐ 中级  
**预计时间**：6-8 小时  
**适合阶段**：完成 Week 2（Day 8-14）后

---

## 📋 项目概述

### 什么是 Docusaurus？

Docusaurus 是 Facebook 开发的静态网站生成器，专为文档站点设计。很多知名项目使用它：
- React 官方文档
- Jest 文档
- LangChain 文档（docs.langchain.com）
- 许多开源项目的文档

### 项目特点

**Docusaurus 文档的特点**：
- 📝 使用 Markdown (.md) 或 MDX (.mdx) 格式
- 🗺️ 通常有 sitemap.xml 文件
- 📂 结构化的目录组织
- 🔗 内部链接丰富
- 🏷️ frontmatter 元数据

**我们要解决的问题**：
- 如何高效爬取整个文档站点？
- 如何保持文档的结构化信息？
- 如何提供准确的答案和引用？

---

## 🏗️ 项目架构

```
Docusaurus 文档站点
        ↓
    爬取模块 (RecursiveUrlLoader / SitemapLoader)
        ↓
    文档处理 (过滤、清洗、分割)
        ↓
    向量化存储 (FAISS / Chroma)
        ↓
    检索系统 (Retriever + Reranking)
        ↓
    问答 Agent (create_agent + RAG)
        ↓
    用户界面 (CLI / Gradio)
```

---

## 📚 核心技术栈

### 1. 文档加载器

**选择1：RecursiveUrlLoader（推荐）**
```python
from langchain_community.document_loaders import RecursiveUrlLoader

loader = RecursiveUrlLoader(
    url="https://docs.example.com/",
    max_depth=3,
    extractor=lambda x: BeautifulSoup(x, "html.parser").text,
    prevent_outside=True,
)
docs = loader.load()
```

**优点**：
- ✅ 递归爬取所有链接
- ✅ 控制爬取深度
- ✅ 自动过滤外部链接

**选择2：SitemapLoader（更快）**
```python
from langchain_community.document_loaders import SitemapLoader

loader = SitemapLoader(
    web_path="https://docs.example.com/sitemap.xml",
)
docs = loader.load()
```

**优点**：
- ✅ 直接从 sitemap 获取所有URL
- ✅ 速度更快
- ✅ 不会遗漏页面

### 2. 文档处理

**文本分割器**：
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""]
)
```

**为什么这样设置**：
- 按 Markdown 标题分割（## 和 ###）
- 保持语义完整性
- 200字符重叠避免信息丢失

### 3. 向量存储

**FAISS（本地，快速）**：
```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

vectorstore = FAISS.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings()
)
```

**Chroma（持久化）**：
```python
from langchain_chroma import Chroma

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(),
    persist_directory="./chroma_db"
)
```

---

## 📖 实战教程

### 阶段 1：基础实现（2-3小时）

#### Step 1：环境准备

```bash
# 创建项目目录
mkdir docusaurus-qa-assistant
cd docusaurus-qa-assistant

# 激活虚拟环境
workon langchain-master  # 或你的环境名

# 安装依赖
pip install langchain langchain-anthropic langchain-openai
pip install langchain-community langgraph
pip install faiss-cpu  # 或 faiss-gpu
pip install beautifulsoup4 lxml
pip install python-dotenv
```

#### Step 2：基础爬虫实现

```python
# 文件：01_load_docs.py

from langchain_community.document_loaders import SitemapLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

def load_docusaurus_docs(sitemap_url: str):
    """从Docusaurus站点加载文档"""
    
    print(f"🔍 开始加载文档: {sitemap_url}")
    
    # 1. 使用 SitemapLoader
    loader = SitemapLoader(
        web_path=sitemap_url,
        filter_urls=[  # 只加载文档页面
            r"https://docs\.example\.com/docs/.*"
        ]
    )
    
    print("📥 正在下载文档...")
    docs = loader.load()
    print(f"✅ 成功加载 {len(docs)} 个文档")
    
    return docs

def process_docs(docs):
    """处理和分割文档"""
    
    print("\n🔨 开始处理文档...")
    
    # 2. 清洗文档
    cleaned_docs = []
    for doc in docs:
        # 移除导航栏、侧边栏等噪音
        content = doc.page_content
        
        # 保留元数据
        metadata = doc.metadata
        metadata['source_url'] = metadata.get('source', '')
        
        cleaned_docs.append(Document(
            page_content=content,
            metadata=metadata
        ))
    
    # 3. 分割文档
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n## ", "\n### ", "\n\n", "\n", " "]
    )
    
    splits = splitter.split_documents(cleaned_docs)
    print(f"✅ 分割成 {len(splits)} 个文档块")
    
    return splits

if __name__ == "__main__":
    # 测试：使用 LangChain 官方文档
    sitemap_url = "https://docs.langchain.com/sitemap.xml"
    
    # 加载文档
    docs = load_docusaurus_docs(sitemap_url)
    
    # 处理文档
    splits = process_docs(docs)
    
    # 显示示例
    print("\n📄 示例文档块:")
    print(f"内容: {splits[0].page_content[:200]}...")
    print(f"元数据: {splits[0].metadata}")
```

#### Step 3：构建向量索引

```python
# 文件：02_build_index.py

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

def build_vectorstore(splits, save_path="vectorstore"):
    """构建向量存储"""
    
    print("\n🔧 构建向量索引...")
    
    # 创建embeddings
    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="text-embedding-3-large"  # 最新模型
    )
    
    # 构建向量存储
    vectorstore = FAISS.from_documents(
        documents=splits,
        embedding=embeddings
    )
    
    print("💾 保存向量索引...")
    
    # 保存到本地
    vectorstore.save_local(save_path)
    
    # 保存文档列表（用于调试）
    with open(f"{save_path}/documents.pkl", "wb") as f:
        pickle.dump(splits, f)
    
    print(f"✅ 向量索引已保存到: {save_path}")
    
    return vectorstore

def load_vectorstore(save_path="vectorstore"):
    """加载向量存储"""
    
    print(f"\n📂 加载向量索引: {save_path}")
    
    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="text-embedding-3-large"
    )
    
    vectorstore = FAISS.load_local(
        save_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    print("✅ 向量索引加载成功")
    
    return vectorstore

def test_retrieval(vectorstore, query: str, k: int = 3):
    """测试检索功能"""
    
    print(f"\n🔍 测试检索: {query}")
    
    # 相似度搜索
    docs = vectorstore.similarity_search(query, k=k)
    
    print(f"\n找到 {len(docs)} 个相关文档:\n")
    
    for i, doc in enumerate(docs, 1):
        print(f"{'='*60}")
        print(f"文档 {i}:")
        print(f"来源: {doc.metadata.get('source_url', 'Unknown')}")
        print(f"内容: {doc.page_content[:200]}...")
        print()
    
    return docs

if __name__ == "__main__":
    from load_docs import load_docusaurus_docs, process_docs
    
    # 1. 加载和处理文档
    sitemap_url = "https://docs.langchain.com/sitemap.xml"
    docs = load_docusaurus_docs(sitemap_url)
    splits = process_docs(docs)
    
    # 2. 构建索引
    vectorstore = build_vectorstore(splits)
    
    # 3. 测试检索
    test_queries = [
        "如何创建一个Agent?",
        "什么是LangGraph?",
        "如何使用memory?"
    ]
    
    for query in test_queries:
        test_retrieval(vectorstore, query)
```

#### Step 4：构建问答Agent

```python
# 文件：03_qa_agent.py

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from build_index import load_vectorstore
import os
from dotenv import load_dotenv

load_dotenv()

class DocusaurusQA:
    """Docusaurus 文档问答助手"""
    
    def __init__(self, vectorstore_path="vectorstore"):
        """初始化"""
        
        print("🚀 初始化 Docusaurus QA 助手...")
        
        # 加载向量存储
        self.vectorstore = load_vectorstore(vectorstore_path)
        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 5}
        )
        
        # 创建模型
        self.model = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        # 创建检索工具
        @tool
        def search_docs(query: str) -> str:
            """在Docusaurus文档中搜索相关信息"""
            docs = self.retriever.invoke(query)
            
            # 格式化结果
            result = []
            for i, doc in enumerate(docs, 1):
                source = doc.metadata.get('source_url', 'Unknown')
                content = doc.page_content
                result.append(f"[来源 {i}: {source}]\n{content}\n")
            
            return "\n---\n".join(result)
        
        # 创建Agent
        self.agent = create_agent(
            model=self.model,
            tools=[search_docs],
            checkpointer=MemorySaver()
        )
        
        print("✅ 助手初始化完成\n")
    
    def ask(self, question: str, thread_id: str = "default") -> dict:
        """提问"""
        
        config = {"configurable": {"thread_id": thread_id}}
        
        result = self.agent.invoke(
            {"messages": question},
            config
        )
        
        return {
            "answer": result["messages"][-1].content,
            "messages": result["messages"]
        }
    
    def chat(self):
        """交互式对话"""
        
        print("💬 进入对话模式（输入 'quit' 退出）\n")
        
        thread_id = "chat-session"
        
        while True:
            question = input("\n你: ").strip()
            
            if question.lower() in ['quit', 'exit', '退出', 'q']:
                print("👋 再见！")
                break
            
            if not question:
                continue
            
            print("\n🤔 思考中...")
            result = self.ask(question, thread_id)
            
            print(f"\n助手: {result['answer']}\n")

if __name__ == "__main__":
    # 创建助手
    qa = DocusaurusQA()
    
    # 测试几个问题
    test_questions = [
        "什么是LangChain？",
        "如何使用create_agent创建Agent？",
        "LangGraph的主要特性有哪些？"
    ]
    
    print("="*60)
    print("测试模式")
    print("="*60)
    
    for q in test_questions:
        print(f"\n❓ {q}")
        result = qa.ask(q)
        print(f"✅ {result['answer'][:300]}...\n")
    
    print("\n" + "="*60)
    print("进入交互模式")
    print("="*60)
    
    # 进入交互模式
    qa.chat()
```

---

### 阶段 2：功能增强（2-3小时）

#### 增强1：文档过滤和清洗

```python
# 文件：advanced/01_doc_cleaner.py

import re
from bs4 import BeautifulSoup
from langchain_core.documents import Document

class DocusaurusDocCleaner:
    """Docusaurus 文档清洗器"""
    
    def __init__(self):
        # 要移除的CSS选择器
        self.remove_selectors = [
            'nav',  # 导航栏
            '.navbar',
            '.sidebar',
            'footer',
            '.table-of-contents',
            '.pagination',
            '.edit-this-page',
            '.theme-doc-breadcrumbs'
        ]
    
    def clean_html(self, html_content: str) -> str:
        """清洗HTML内容"""
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 移除不需要的元素
        for selector in self.remove_selectors:
            for element in soup.select(selector):
                element.decompose()
        
        # 提取主要内容
        main_content = soup.find('article') or soup.find('main') or soup
        
        # 获取文本
        text = main_content.get_text(separator='\n', strip=True)
        
        # 清理多余空行
        text = re.sub(r'\n\s*\n+', '\n\n', text)
        
        return text
    
    def extract_metadata(self, html_content: str, url: str) -> dict:
        """提取元数据"""
        
        soup = BeautifulSoup(html_content, 'html.parser')
        metadata = {'source_url': url}
        
        # 提取标题
        title = soup.find('h1')
        if title:
            metadata['title'] = title.get_text(strip=True)
        
        # 提取描述
        desc = soup.find('meta', {'name': 'description'})
        if desc:
            metadata['description'] = desc.get('content', '')
        
        # 提取关键词
        keywords = soup.find('meta', {'name': 'keywords'})
        if keywords:
            metadata['keywords'] = keywords.get('content', '')
        
        return metadata
    
    def clean_document(self, doc: Document) -> Document:
        """清洗单个文档"""
        
        # 假设 page_content 是 HTML
        clean_text = self.clean_html(doc.page_content)
        
        # 提取元数据
        metadata = self.extract_metadata(
            doc.page_content,
            doc.metadata.get('source', '')
        )
        
        # 合并现有元数据
        metadata.update(doc.metadata)
        
        return Document(
            page_content=clean_text,
            metadata=metadata
        )
```

#### 增强2：智能分割

```python
# 文件：advanced/02_smart_splitter.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import re

class MarkdownAwareSplitter:
    """Markdown 感知的文档分割器"""
    
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Markdown 层级分隔符
        self.separators = [
            "\n## ",      # H2 标题
            "\n### ",     # H3 标题
            "\n#### ",    # H4 标题
            "\n\n",       # 段落
            "\n",         # 行
            " ",          # 词
            ""            # 字符
        ]
    
    def split_documents(self, documents: list[Document]) -> list[Document]:
        """分割文档"""
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=self.separators,
            keep_separator=True  # 保留分隔符
        )
        
        splits = []
        
        for doc in documents:
            # 分割
            doc_splits = splitter.split_documents([doc])
            
            # 为每个块添加额外的元数据
            for i, split in enumerate(doc_splits):
                # 提取当前块的标题
                title = self._extract_title(split.page_content)
                if title:
                    split.metadata['section_title'] = title
                
                split.metadata['chunk_index'] = i
                split.metadata['total_chunks'] = len(doc_splits)
                
                splits.append(split)
        
        return splits
    
    def _extract_title(self, text: str) -> str:
        """提取文本中的标题"""
        
        # 匹配 Markdown 标题
        match = re.search(r'^#+ (.+)$', text, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        return ""
```

#### 增强3：混合检索（Hybrid Retrieval）

```python
# 文件：advanced/03_hybrid_retrieval.py

from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document

class HybridRetriever:
    """混合检索器：结合向量检索和关键词检索"""
    
    def __init__(self, vectorstore, documents: list[Document]):
        """
        vectorstore: 向量存储
        documents: 原始文档列表
        """
        
        # 向量检索器
        self.vector_retriever = vectorstore.as_retriever(
            search_kwargs={"k": 5}
        )
        
        # BM25 检索器（关键词）
        self.bm25_retriever = BM25Retriever.from_documents(documents)
        self.bm25_retriever.k = 5
        
        # 混合检索器
        self.ensemble = EnsembleRetriever(
            retrievers=[self.vector_retriever, self.bm25_retriever],
            weights=[0.6, 0.4]  # 向量检索权重60%，BM25权重40%
        )
    
    def invoke(self, query: str) -> list[Document]:
        """检索文档"""
        return self.ensemble.invoke(query)
```

#### 增强4：答案引用

```python
# 文件：advanced/04_answer_with_citations.py

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
import os

class QAWithCitations:
    """带引用的问答系统"""
    
    def __init__(self, retriever):
        self.retriever = retriever
        self.model = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        # 创建检索工具
        @tool
        def search_with_sources(query: str) -> str:
            """搜索文档并返回带来源的结果"""
            docs = self.retriever.invoke(query)
            
            result = []
            for i, doc in enumerate(docs, 1):
                source = doc.metadata.get('source_url', 'Unknown')
                title = doc.metadata.get('title', 'Untitled')
                content = doc.page_content
                
                result.append(
                    f"[来源{i}] {title}\n"
                    f"链接: {source}\n"
                    f"内容: {content}\n"
                )
            
            return "\n---\n".join(result)
        
        # 创建Agent，使用特殊提示词
        self.agent = create_agent(
            model=self.model,
            tools=[search_with_sources],
        )
    
    def ask_with_citations(self, question: str) -> dict:
        """提问并获取带引用的答案"""
        
        # 特殊的系统提示
        system_prompt = """你是一个文档助手。在回答问题时：

1. 使用检索工具搜索相关信息
2. 在答案中明确引用来源，格式为 [来源X]
3. 在答案末尾列出所有引用的链接
4. 如果信息不确定，明确说明

示例回答格式：
根据文档，LangChain 是一个用于构建LLM应用的框架[来源1]。它提供了多种工具和抽象[来源2]。

参考链接：
[来源1] https://docs.langchain.com/intro
[来源2] https://docs.langchain.com/concepts
"""
        
        result = self.agent.invoke({
            "messages": [
                ("system", system_prompt),
                ("user", question)
            ]
        })
        
        return {
            "answer": result["messages"][-1].content,
            "raw_messages": result["messages"]
        }
```

---

### 阶段 3：用户界面（2小时）

#### UI 选项1：命令行界面（CLI）

```python
# 文件：ui/cli_app.py

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from qa_agent import DocusaurusQA

console = Console()

def main():
    """CLI 主程序"""
    
    console.print(Panel.fit(
        "[bold cyan]Docusaurus 文档智能问答助手[/bold cyan]",
        subtitle="输入问题开始对话，输入 'quit' 退出"
    ))
    
    # 初始化助手
    with console.status("[bold green]正在初始化助手..."):
        qa = DocusaurusQA()
    
    thread_id = "cli-session"
    
    while True:
        console.print()
        question = console.input("[bold yellow]你: [/bold yellow]")
        
        if question.lower() in ['quit', 'exit', '退出']:
            console.print("[bold red]再见！[/bold red]")
            break
        
        if not question.strip():
            continue
        
        # 获取答案
        with console.status("[bold green]思考中..."):
            result = qa.ask(question, thread_id)
        
        # 显示答案
        console.print("[bold cyan]助手:[/bold cyan]")
        console.print(Markdown(result['answer']))

if __name__ == "__main__":
    main()
```

#### UI 选项2：Web界面（Gradio）

```python
# 文件：ui/web_app.py

import gradio as gr
from qa_agent import DocusaurusQA
import os

# 初始化助手
qa = DocusaurusQA()

def chat_interface(message, history):
    """聊天接口"""
    
    # 使用session作为thread_id
    thread_id = "gradio-session"
    
    # 获取答案
    result = qa.ask(message, thread_id)
    
    return result['answer']

# 创建界面
with gr.Blocks(title="Docusaurus 文档助手", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 📚 Docusaurus 文档智能问答助手
    
    基于 LangChain 和 Claude 构建的文档问答系统
    """)
    
    chatbot = gr.ChatInterface(
        chat_interface,
        chatbot=gr.Chatbot(height=500),
        textbox=gr.Textbox(
            placeholder="输入你的问题...",
            container=False,
            scale=7
        ),
        title=None,
        examples=[
            "什么是 LangChain？",
            "如何创建一个 Agent？",
            "LangGraph 的主要特性有哪些？",
            "如何使用 memory 管理对话历史？"
        ],
        cache_examples=False,
    )
    
    gr.Markdown("""
    ---
    💡 **提示**: 你可以连续提问，系统会记住对话上下文
    """)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
```

---

## 🎯 完整项目结构

```
docusaurus-qa-assistant/
├── .env                          # API keys
├── requirements.txt              # 依赖
│
├── 基础模块/
│   ├── 01_load_docs.py          # 文档加载
│   ├── 02_build_index.py        # 索引构建
│   └── 03_qa_agent.py           # 问答Agent
│
├── advanced/                     # 高级功能
│   ├── 01_doc_cleaner.py        # 文档清洗
│   ├── 02_smart_splitter.py     # 智能分割
│   ├── 03_hybrid_retrieval.py   # 混合检索
│   └── 04_answer_with_citations.py  # 带引用
│
├── ui/                           # 用户界面
│   ├── cli_app.py               # CLI
│   └── web_app.py               # Web (Gradio)
│
├── vectorstore/                  # 向量存储（生成）
│   ├── index.faiss
│   └── index.pkl
│
└── docs/                         # 项目文档
    ├── README.md
    └── DEPLOYMENT.md
```

---

## 📝 作业任务

### 必做任务

1. **基础实现** (必需)
   - [ ] 完成文档加载和索引构建
   - [ ] 实现基础的问答功能
   - [ ] 测试至少3个问题

2. **选择一个增强功能** (任选其一)
   - [ ] 选项A: 实现文档清洗
   - [ ] 选项B: 实现混合检索
   - [ ] 选项C: 实现答案引用

3. **用户界面** (任选其一)
   - [ ] 选项A: CLI 界面
   - [ ] 选项B: Gradio Web 界面

### 加分任务

4. **高级功能** (可选)
   - [ ] 实现多语言支持
   - [ ] 添加对话历史导出
   - [ ] 实现文档更新检测
   - [ ] 添加问题推荐功能

5. **优化** (可选)
   - [ ] 实现缓存机制
   - [ ] 优化检索速度
   - [ ] 添加流式输出

---

## ✅ 评估标准

### 功能完整性（40分）
- 能正确加载 Docusaurus 文档
- 检索功能工作正常
- 问答准确且相关

### 代码质量（30分）
- 代码结构清晰
- 有适当的错误处理
- 有必要的注释

### 用户体验（20分）
- 界面友好
- 响应及时
- 提示信息清晰

### 创新性（10分）
- 实现了额外功能
- 有独特的优化
- 解决了实际问题

---

## 🚀 部署建议

### 本地部署

```bash
# 1. 构建索引（只需一次）
python 01_load_docs.py
python 02_build_index.py

# 2. 运行应用
# CLI版本
python ui/cli_app.py

# Web版本
python ui/web_app.py
```

### Docker 部署

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "ui/web_app.py"]
```

---

## 💡 学习要点

通过这个项目，你将学会：

1. **文档处理**
   - 如何爬取和清洗文档
   - 如何智能分割文档
   - 如何保持文档结构

2. **RAG 系统**
   - 如何构建向量索引
   - 如何实现高效检索
   - 如何优化检索质量

3. **Agent 开发**
   - 如何使用 create_agent
   - 如何设计工具
   - 如何管理对话上下文

4. **生产实践**
   - 如何优化性能
   - 如何处理错误
   - 如何设计用户界面

---

## 📚 参考资源

- [LangChain Document Loaders](https://python.langchain.com/docs/integrations/document_loaders/)
- [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [FAISS Vector Store](https://python.langchain.com/docs/integrations/vectorstores/faiss/)
- [Gradio 文档](https://www.gradio.app/docs/)

---

**开始你的项目吧！** 🚀

有问题随时参考文档或寻求帮助。记住：实践是最好的老师！
