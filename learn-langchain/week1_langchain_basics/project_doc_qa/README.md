# Week 1 Project: 智能文档问答助手

> 构建一个完整的文档问答系统

## 🎯 项目目标

构建一个智能文档问答助手，支持：
- 加载多种格式文档（txt, md）
- 智能分割文本
- 基于文档内容的问答
- 引用来源信息
- 友好的CLI交互界面

## 📋 功能需求

### 基础功能
- [ ] 加载txt和md格式文档
- [ ] 文本分割和处理
- [ ] 基于内容的问答
- [ ] CLI交互界面

### 进阶功能（可选）
- [ ] 支持多个文档
- [ ] 引用来源信息
- [ ] 对话历史记录
- [ ] 输出美化

## 🏗️ 项目结构

```
project_doc_qa/
├── README.md              # 本文件
├── requirements.txt       # 项目依赖
├── .env.example          # 环境变量模板
├── main.py               # 主程序入口
├── doc_loader.py         # 文档加载模块
├── qa_system.py          # 问答系统模块
├── utils.py              # 工具函数
├── docs/                 # 示例文档目录
│   ├── sample1.txt
│   └── sample2.md
└── tests/                # 测试文件（可选）
    └── test_qa.py
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install langchain langchain-anthropic python-dotenv
```

### 2. 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env，填入你的 API Key
# ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### 3. 准备文档

将你要问答的文档放在 `docs/` 目录下。

### 4. 运行程序

```bash
python main.py
```

## 💻 实现步骤

### Step 1: 文档加载 (doc_loader.py)

实现文档加载功能：
```python
def load_document(file_path: str) -> str:
    """加载文档内容"""
    pass

def split_text(text: str, chunk_size: int = 500) -> list[str]:
    """分割文本"""
    pass
```

### Step 2: 问答系统 (qa_system.py)

实现问答逻辑：
```python
class DocumentQA:
    def __init__(self, documents: list[str]):
        """初始化问答系统"""
        pass
    
    def ask(self, question: str) -> str:
        """回答问题"""
        pass
```

### Step 3: 主程序 (main.py)

整合所有功能，提供CLI界面。

## 📝 实现提示

### 文档加载提示
- 使用 `open()` 读取文件
- 处理不同编码（utf-8, gbk等）
- 考虑文件不存在的情况

### 文本分割提示
- 简单方法：按字符数分割
- 进阶方法：按段落或句子分割
- 保持语义完整性

### 问答提示
- 使用之前学过的消息系统
- 将文档内容加入Prompt
- 设计好的系统提示词

### Prompt设计示例
```python
system_prompt = f"""你是一个文档问答助手。
请根据以下文档内容回答用户的问题。

文档内容：
{document_content}

回答要求：
1. 只根据文档内容回答
2. 如果文档中没有相关信息，请说"文档中没有找到相关信息"
3. 保持回答简洁准确
"""
```

## ✅ 评估标准

### 基础分（60分）
- [ ] 能加载文档（10分）
- [ ] 能回答基于文档的问题（30分）
- [ ] CLI界面友好（10分）
- [ ] 代码规范，有注释（10分）

### 进阶分（30分）
- [ ] 支持多个文档（10分）
- [ ] 文本分割合理（10分）
- [ ] 引用来源信息（10分）

### 加分项（10分）
- [ ] 完善的错误处理（3分）
- [ ] 对话历史记录（3分）
- [ ] 输出美化（2分）
- [ ] 测试用例（2分）

## 🎯 学习目标检查

完成这个项目后，你应该能够：
- [ ] 独立读取和处理文本文件
- [ ] 设计合适的Prompt来完成特定任务
- [ ] 使用LangChain构建完整的应用
- [ ] 理解基础的RAG（检索增强生成）概念
- [ ] 创建友好的用户界面

## 💡 扩展思路

完成基础功能后，可以尝试：
1. 添加PDF文档支持
2. 实现文档摘要功能
3. 支持批量文档查询
4. 添加Web界面
5. 实现对话历史搜索

## 📚 参考资料

- [LangChain文档加载](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Prompt工程最佳实践](https://docs.anthropic.com/claude/docs/prompt-engineering)

## 🆘 常见问题

### Q1: 文档太长怎么办？
- 将文档分割成小块
- 只传递相关部分给LLM
- 考虑使用向量检索（Week 2会学习）

### Q2: 回答不准确？
- 优化系统提示词
- 改进文本分割策略
- 在Prompt中强调"根据文档回答"

### Q3: 如何引用来源？
- 记录文本块的来源
- 在回答中添加文档引用
- 提供原文摘录

## 🎉 完成标志

当你能运行程序并：
1. 成功加载文档
2. 准确回答基于文档的问题
3. 有友好的交互界面

恭喜你完成了Week 1的项目！🎊

---

**祝你开发顺利！有问题随时查看课程材料或在社区提问。** 💪
