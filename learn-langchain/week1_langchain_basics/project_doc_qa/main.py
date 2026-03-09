"""
智能文档问答助手 - 主程序

这是Week 1的项目作业，你需要：
1. 实现文档加载功能
2. 实现问答功能
3. 创建友好的CLI界面

提示：
- 查看 README.md 了解项目需求
- 参考 Day 1-6 的示例代码
- 逐步实现，先完成基础功能
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 加载环境变量
load_dotenv()

# ============================================================================
# TODO: 实现文档加载功能
# ============================================================================

def load_document(file_path: str) -> str:
    """
    加载文档内容
    
    Args:
        file_path: 文档路径
    
    Returns:
        文档内容（字符串）
    
    提示：
    - 使用 open() 读取文件
    - 处理可能的编码问题
    - 处理文件不存在的情况
    """
    # TODO: 在这里实现文档加载逻辑
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"❌ 文件不存在: {file_path}")
        return ""
    except Exception as e:
        print(f"❌ 读取文件出错: {str(e)}")
        return ""

def load_all_documents(docs_dir: str = "docs") -> dict:
    """
    加载目录下的所有文档
    
    Args:
        docs_dir: 文档目录路径
    
    Returns:
        字典，键为文件名，值为文档内容
    """
    # TODO: 实现加载多个文档的逻辑
    documents = {}
    
    if not os.path.exists(docs_dir):
        print(f"❌ 目录不存在: {docs_dir}")
        return documents
    
    for filename in os.listdir(docs_dir):
        if filename.endswith(('.txt', '.md')):
            file_path = os.path.join(docs_dir, filename)
            content = load_document(file_path)
            if content:
                documents[filename] = content
                print(f"✅ 已加载: {filename}")
    
    return documents

# ============================================================================
# TODO: 实现文本分割功能（可选）
# ============================================================================

def split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    将长文本分割成小块
    
    Args:
        text: 要分割的文本
        chunk_size: 每块的大小
        overlap: 块之间的重叠大小
    
    Returns:
        文本块列表
    
    提示：
    - 简单方法：按字符数分割
    - 进阶方法：按段落或句子分割
    - 考虑重叠以保持上下文连贯
    """
    # TODO: 实现文本分割逻辑（可选）
    # 简单实现：按字符数分割
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

# ============================================================================
# TODO: 实现问答系统
# ============================================================================

class DocumentQA:
    """
    文档问答系统
    """
    
    def __init__(self, documents: dict):
        """
        初始化问答系统
        
        Args:
            documents: 文档字典，{文件名: 文档内容}
        """
        self.documents = documents
        self.model = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.3  # 降低温度以获得更准确的答案
        )
        self.conversation_history = []
        
        # TODO: 准备文档内容
        self.doc_content = self._prepare_documents()
    
    def _prepare_documents(self) -> str:
        """
        准备文档内容，格式化为字符串
        
        Returns:
            格式化的文档内容
        """
        # TODO: 将所有文档合并为一个字符串
        if not self.documents:
            return "（没有加载任何文档）"
        
        content_parts = []
        for filename, content in self.documents.items():
            content_parts.append(f"[文档: {filename}]\n{content}\n")
        
        return "\n".join(content_parts)
    
    def _create_system_prompt(self) -> str:
        """
        创建系统提示词
        
        Returns:
            系统提示词
        
        提示：
        - 明确告诉AI它的角色
        - 提供文档内容
        - 设定回答规则
        """
        # TODO: 设计一个好的系统提示词
        return f"""你是一个专业的文档问答助手。

你的任务是根据以下文档内容回答用户的问题。

【文档内容】
{self.doc_content}

【回答规则】
1. 只根据上述文档内容回答问题
2. 如果文档中没有相关信息，明确告诉用户"文档中没有找到相关信息"
3. 回答要准确、简洁
4. 可以引用文档中的原文
5. 保持友好和专业的语气
"""
    
    def ask(self, question: str) -> str:
        """
        回答问题
        
        Args:
            question: 用户的问题
        
        Returns:
            AI的回答
        """
        # TODO: 实现问答逻辑
        try:
            # 构建消息
            messages = [
                SystemMessage(content=self._create_system_prompt()),
                HumanMessage(content=question)
            ]
            
            # 调用模型
            response = self.model.invoke(messages)
            
            return response.content
        
        except Exception as e:
            return f"❌ 出错了: {str(e)}"
    
    def chat(self):
        """
        启动交互式问答
        """
        print("\n" + "="*70)
        print("📚 智能文档问答助手")
        print("="*70)
        print(f"\n已加载 {len(self.documents)} 个文档：")
        for filename in self.documents.keys():
            print(f"  - {filename}")
        print("\n输入问题开始提问，输入 'quit' 退出\n")
        
        while True:
            # 获取用户输入
            question = input("💭 你的问题: ").strip()
            
            # 检查退出命令
            if question.lower() in ['quit', 'exit', '退出', 'q']:
                print("\n👋 再见！")
                break
            
            # 跳过空输入
            if not question:
                continue
            
            # 回答问题
            print("\n🤔 思考中...\n")
            answer = self.ask(question)
            print(f"✨ 回答: {answer}\n")
            print("-" * 70)

# ============================================================================
# 主函数
# ============================================================================

def main():
    """
    主函数
    """
    print("\n" + "="*70)
    print("🎓 Week 1 项目: 智能文档问答助手")
    print("="*70)
    
    # 检查API Key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("\n❌ 错误: 未找到 ANTHROPIC_API_KEY")
        print("请在 .env 文件中配置 API Key")
        return
    
    # 加载文档
    print("\n📖 正在加载文档...")
    documents = load_all_documents("docs")
    
    if not documents:
        print("\n❌ 没有找到任何文档")
        print("请在 docs/ 目录下放置 .txt 或 .md 文件")
        return
    
    print(f"\n✅ 成功加载 {len(documents)} 个文档")
    
    # 创建问答系统
    qa_system = DocumentQA(documents)
    
    # 开始交互
    qa_system.chat()

if __name__ == "__main__":
    main()
