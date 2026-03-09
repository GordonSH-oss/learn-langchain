# DeepAgents 完全指南

> 深入学习 DeepAgents 框架，构建强大的多 Agent 系统

## 📋 目录

- [概述](#概述)
- [与 LangChain 的关系](#与-langchain-的关系)
- [核心概念](#核心概念)
- [快速开始](#快速开始)
- [深入教程](#深入教程)
- [高级特性](#高级特性)
- [实战项目](#实战项目)
- [最佳实践](#最佳实践)

---

## 📖 概述

### 什么是 DeepAgents？

DeepAgents 是一个高级 Agent 框架，专注于：
- 🤖 **多 Agent 协作** - 轻松构建协作系统
- 🔄 **复杂工作流** - 支持复杂的决策流程
- 🎯 **任务规划** - 自动任务分解和分配
- 📊 **状态管理** - 强大的状态追踪能力

### 为什么使用 DeepAgents？

| 特性 | LangChain | LangGraph | DeepAgents |
|------|-----------|-----------|------------|
| 简单任务 | ✅✅✅ | ✅✅ | ✅✅ |
| 复杂工作流 | ✅ | ✅✅✅ | ✅✅✅ |
| 多 Agent | ❌ | ✅✅ | ✅✅✅ |
| 开箱即用 | ✅✅✅ | ✅✅ | ✅✅✅ |
| 学习曲线 | 低 | 中 | 中 |

---

## 🔗 与 LangChain 的关系

DeepAgents 基于 LangChain 和 LangGraph 构建，提供了更高级别的抽象：

```
┌─────────────────────────────────┐
│       DeepAgents               │  高级抽象
│  (多Agent、规划、协作)          │
├─────────────────────────────────┤
│       LangGraph                │  状态图
│  (状态机、工作流)               │
├─────────────────────────────────┤
│       LangChain                │  基础组件
│  (LLM、Chain、Tools)            │
└─────────────────────────────────┘
```

**集成优势**：
- 可以使用所有 LangChain 的工具
- 可以嵌入 LangGraph 的状态图
- 可以混合使用三个框架

---

## 🎯 核心概念

### 1. Agent（智能体）

Agent 是具有自主决策能力的实体：

```python
from deepagents import Agent

# 创建一个专家 Agent
code_expert = Agent(
    name="CodeExpert",
    role="高级 Python 开发工程师",
    goal="审查和优化 Python 代码",
    backstory="拥有10年Python开发经验，擅长性能优化和最佳实践",
    tools=[code_analysis_tool, linting_tool],
    llm=model
)
```

**Agent 属性**：
- `name` - Agent 名称
- `role` - 角色定义
- `goal` - 目标
- `backstory` - 背景故事（影响 Agent 行为）
- `tools` - 可用工具列表
- `llm` - 使用的语言模型
- `max_iter` - 最大迭代次数
- `verbose` - 是否输出详细信息

### 2. Task（任务）

Task 定义了 Agent 要完成的工作：

```python
from deepagents import Task

review_task = Task(
    description="审查以下 Python 代码，找出潜在问题和优化建议：\n{code}",
    expected_output="详细的代码审查报告，包含问题列表和改进建议",
    agent=code_expert,
    context=[previous_task],  # 依赖的前置任务
)
```

**Task 属性**：
- `description` - 任务描述
- `expected_output` - 期望输出
- `agent` - 执行该任务的 Agent
- `context` - 上下文任务（依赖关系）
- `async_execution` - 是否异步执行
- `callback` - 完成回调

### 3. Crew（团队）

Crew 管理多个 Agent 的协作：

```python
from deepagents import Crew, Process

crew = Crew(
    agents=[code_expert, test_engineer, reviewer],
    tasks=[code_task, test_task, review_task],
    process=Process.sequential,  # 或 Process.hierarchical
    verbose=True
)

result = crew.kickoff(inputs={"code": source_code})
```

**协作模式**：
- `sequential` - 顺序执行
- `hierarchical` - 分层管理
- `parallel` - 并行执行（实验性）

---

## 🚀 快速开始

### 环境准备

```bash
# 激活虚拟环境
workon langchain

# 安装 DeepAgents
pip install deepagents

# 确认安装
python -c "import deepagents; print(deepagents.__version__)"
```

### 第一个 DeepAgents 应用

```python
# 文件：deepagents_examples/01_hello_deepagents.py

from deepagents import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

# 初始化模型
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创建研究员 Agent
researcher = Agent(
    name="Researcher",
    role="技术研究员",
    goal="研究和总结技术主题",
    backstory="专注于深度技术研究的工程师",
    llm=model,
    verbose=True
)

# 创建写作 Agent
writer = Agent(
    name="Writer",
    role="技术作家",
    goal="将研究结果写成易懂的文章",
    backstory="擅长将复杂技术转化为通俗内容的作家",
    llm=model,
    verbose=True
)

# 定义任务
research_task = Task(
    description="研究 {topic} 的最新发展和核心概念",
    expected_output="详细的研究报告，包含关键概念和最新进展",
    agent=researcher
)

writing_task = Task(
    description="基于研究报告，写一篇面向开发者的技术文章",
    expected_output="1000字左右的技术文章，包含标题、摘要和正文",
    agent=writer,
    context=[research_task]  # 依赖研究任务
)

# 创建团队
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True
)

# 执行
if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": "LangChain Agent"})
    
    print("\n" + "="*50)
    print("最终结果:")
    print("="*50)
    print(result)
```

**运行**：
```bash
python deepagents_examples/01_hello_deepagents.py
```

**预期输出**：
1. Researcher 开始研究 LangChain Agent
2. Writer 基于研究结果写文章
3. 输出最终文章

---

## 📚 深入教程

### 教程 1：创建带工具的 Agent

```python
# 文件：deepagents_examples/02_agent_with_tools.py

from deepagents import Agent, Task, Crew
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# 创建工具
@tool
def search_wikipedia(query: str) -> str:
    """在维基百科搜索信息"""
    # 简化实现，实际应使用 Wikipedia API
    return f"关于 {query} 的维基百科信息..."

@tool
def calculate(expression: str) -> float:
    """计算数学表达式"""
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"计算错误: {str(e)}"

@tool
def get_current_time() -> str:
    """获取当前时间"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 创建研究 Agent（带工具）
researcher = Agent(
    name="ResearchAgent",
    role="研究助手",
    goal="使用工具查找和验证信息",
    backstory="能够使用多种工具进行研究的助手",
    tools=[search_wikipedia, calculate, get_current_time],
    llm=ChatAnthropic(
        model="claude-3-5-sonnet-20241022",
        api_key=os.getenv("ANTHROPIC_API_KEY")
    ),
    verbose=True
)

# 创建任务
task = Task(
    description="""
    回答以下问题：
    1. LangChain 是什么时候发布的？
    2. 如果今天是 2024年，那么 LangChain 已经发布多少年了？(计算：2024 - 2022)
    3. 现在的具体时间是多少？
    
    请使用可用的工具来回答这些问题。
    """,
    expected_output="包含所有问题答案的报告",
    agent=researcher
)

# 执行
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()

print("\n结果:", result)
```

---

### 教程 2：层级协作（Hierarchical）

```python
# 文件：deepagents_examples/03_hierarchical_crew.py

from deepagents import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创建多个专家 Agent
frontend_expert = Agent(
    name="FrontendExpert",
    role="前端开发专家",
    goal="设计和实现用户界面",
    backstory="10年前端开发经验，精通 React 和现代前端技术",
    llm=model
)

backend_expert = Agent(
    name="BackendExpert",
    role="后端开发专家",
    goal="设计和实现后端 API",
    backstory="精通 Python、数据库和 API 设计",
    llm=model
)

devops_expert = Agent(
    name="DevOpsExpert",
    role="DevOps 工程师",
    goal="负责部署和运维",
    backstory="精通 Docker、Kubernetes 和 CI/CD",
    llm=model
)

# 创建经理 Agent（可选，hierarchical 模式会自动创建）
manager = Agent(
    name="ProjectManager",
    role="项目经理",
    goal="协调团队完成项目",
    backstory="经验丰富的技术项目经理",
    llm=model,
    allow_delegation=True  # 允许委托任务
)

# 定义任务
task1 = Task(
    description="设计一个 Todo 应用的前端界面，包含任务列表、添加任务、完成任务等功能",
    expected_output="前端设计方案，包含组件结构和主要功能",
    agent=frontend_expert
)

task2 = Task(
    description="设计 Todo 应用的后端 API，包含 CRUD 操作",
    expected_output="API 设计文档，包含端点、请求格式和响应格式",
    agent=backend_expert
)

task3 = Task(
    description="设计部署方案，包含 Docker 配置和 CI/CD 流程",
    expected_output="部署文档和配置文件",
    agent=devops_expert,
    context=[task1, task2]  # 依赖前两个任务
)

# 创建层级团队
crew = Crew(
    agents=[frontend_expert, backend_expert, devops_expert],
    tasks=[task1, task2, task3],
    process=Process.hierarchical,  # 层级模式
    manager_llm=model,  # 经理使用的模型
    verbose=True
)

# 执行
result = crew.kickoff()

print("\n" + "="*50)
print("项目方案:")
print("="*50)
print(result)
```

**Hierarchical 模式特点**：
- 自动创建 Manager Agent
- Manager 负责任务分配和协调
- Agent 向 Manager 报告进度
- Manager 做最终决策

---

### 教程 3：异步任务执行

```python
# 文件：deepagents_examples/04_async_tasks.py

from deepagents import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
import time

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创建多个 Agent
agent1 = Agent(
    name="DataCollector",
    role="数据收集员",
    goal="收集用户数据",
    llm=model
)

agent2 = Agent(
    name="DataAnalyzer",
    role="数据分析师",
    goal="分析数据模式",
    llm=model
)

agent3 = Agent(
    name="ReportWriter",
    role="报告撰写员",
    goal="生成分析报告",
    llm=model
)

# 创建任务
collect_task = Task(
    description="收集过去一周的用户活动数据",
    expected_output="用户活动数据摘要",
    agent=agent1,
    async_execution=False  # 同步执行
)

# 这两个任务可以并行
analyze_behavior = Task(
    description="分析用户行为模式",
    expected_output="行为分析报告",
    agent=agent2,
    context=[collect_task],
    async_execution=True  # 异步执行
)

analyze_trends = Task(
    description="分析用户活跃趋势",
    expected_output="趋势分析报告",
    agent=agent2,
    context=[collect_task],
    async_execution=True  # 异步执行
)

# 汇总任务
report_task = Task(
    description="基于行为分析和趋势分析，生成综合报告",
    expected_output="完整的数据分析报告",
    agent=agent3,
    context=[analyze_behavior, analyze_trends],
    async_execution=False
)

# 创建团队
crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[collect_task, analyze_behavior, analyze_trends, report_task],
    process=Process.sequential,
    verbose=True
)

# 执行
start_time = time.time()
result = crew.kickoff()
end_time = time.time()

print(f"\n执行时间: {end_time - start_time:.2f}秒")
print("\n最终报告:")
print(result)
```

---

### 教程 4：Agent 间通信

```python
# 文件：deepagents_examples/05_agent_communication.py

from deepagents import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创建对话 Agent
teacher = Agent(
    name="Teacher",
    role="编程导师",
    goal="教授编程概念",
    backstory="经验丰富的编程教师，善于解释复杂概念",
    llm=model,
    verbose=True
)

student = Agent(
    name="Student",
    role="学生",
    goal="学习编程并提出问题",
    backstory="对编程充满好奇的初学者",
    llm=model,
    verbose=True
)

reviewer = Agent(
    name="Reviewer",
    role="教学评审员",
    goal="评估教学质量",
    backstory="教育专家，负责确保教学效果",
    llm=model,
    verbose=True
)

# Task 1: 老师讲解
teach_task = Task(
    description="向学生解释什么是 Python 装饰器，并给出示例",
    expected_output="清晰的装饰器讲解和代码示例",
    agent=teacher
)

# Task 2: 学生提问
question_task = Task(
    description="基于老师的讲解，提出 2-3 个深入的问题",
    expected_output="学生的问题列表",
    agent=student,
    context=[teach_task]
)

# Task 3: 老师回答
answer_task = Task(
    description="回答学生提出的问题",
    expected_output="详细的问题解答",
    agent=teacher,
    context=[question_task]
)

# Task 4: 评审
review_task = Task(
    description="评估整个教学过程的效果，包括讲解质量、问题质量和回答质量",
    expected_output="教学质量评估报告",
    agent=reviewer,
    context=[teach_task, question_task, answer_task]
)

# 创建团队
crew = Crew(
    agents=[teacher, student, reviewer],
    tasks=[teach_task, question_task, answer_task, review_task],
    process=Process.sequential,
    verbose=True
)

# 执行
result = crew.kickoff()

print("\n" + "="*50)
print("教学总结:")
print("="*50)
print(result)
```

---

## 🎨 高级特性

### 1. 记忆系统

DeepAgents 支持多种记忆类型：

```python
from deepagents.memory import (
    ShortTermMemory,
    LongTermMemory,
    EntityMemory
)

agent = Agent(
    name="MemoryAgent",
    role="助手",
    memory=True,  # 启用短期记忆
    long_term_memory=LongTermMemory(),  # 长期记忆
    entity_memory=EntityMemory(),  # 实体记忆
    llm=model
)
```

**记忆类型**：
- **Short-term Memory** - 当前会话的记忆
- **Long-term Memory** - 跨会话的持久记忆
- **Entity Memory** - 关于特定实体的记忆

---

### 2. 人工反馈（Human-in-the-Loop）

```python
from deepagents import Agent, Task, Crew

agent = Agent(
    name="Assistant",
    role="助手",
    llm=model
)

task = Task(
    description="创建一个营销方案",
    expected_output="完整的营销方案",
    agent=agent,
    human_input=True  # 需要人工确认
)

crew = Crew(agents=[agent], tasks=[task])

# 执行时会暂停等待人工输入
result = crew.kickoff()
```

---

### 3. 工具集成（高级）

```python
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class DatabaseQueryInput(BaseModel):
    """数据库查询输入"""
    query: str = Field(description="SQL 查询语句")

class DatabaseQueryTool(BaseTool):
    name = "database_query"
    description = "执行数据库查询"
    args_schema = DatabaseQueryInput
    
    def _run(self, query: str) -> str:
        """执行查询"""
        # 实际实现
        return f"查询结果: {query}"
    
    async def _arun(self, query: str) -> str:
        """异步执行"""
        return self._run(query)

# 使用自定义工具
agent = Agent(
    name="DataAgent",
    role="数据分析师",
    tools=[DatabaseQueryTool()],
    llm=model
)
```

---

### 4. 自定义流程

```python
from deepagents import Crew, Process

class CustomProcess(Process):
    """自定义流程"""
    
    def execute(self, tasks, agents):
        """自定义执行逻辑"""
        # 实现自定义的任务执行流程
        results = []
        
        for task in tasks:
            # 自定义的任务分配逻辑
            agent = self.select_agent(task, agents)
            result = agent.execute(task)
            results.append(result)
        
        return self.aggregate_results(results)
    
    def select_agent(self, task, agents):
        """选择合适的 Agent"""
        # 实现选择逻辑
        pass
    
    def aggregate_results(self, results):
        """聚合结果"""
        # 实现聚合逻辑
        pass

# 使用自定义流程
crew = Crew(
    agents=agents,
    tasks=tasks,
    process=CustomProcess(),
    verbose=True
)
```

---

## 💡 实战项目

### 项目 1：智能代码审查系统

```python
# 文件：deepagents_examples/project_code_review.py

from deepagents import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 工具
@tool
def run_linter(code: str) -> str:
    """运行代码检查工具"""
    # 简化实现
    return "Linting 结果: 代码格式良好"

@tool
def run_tests(code: str) -> str:
    """运行测试"""
    return "测试结果: 所有测试通过"

@tool
def check_security(code: str) -> str:
    """安全检查"""
    return "安全检查: 未发现安全问题"

# Agent 团队
syntax_checker = Agent(
    name="SyntaxChecker",
    role="语法检查员",
    goal="检查代码语法和格式",
    tools=[run_linter],
    llm=model
)

logic_reviewer = Agent(
    name="LogicReviewer",
    role="逻辑审查员",
    goal="审查代码逻辑和算法",
    llm=model
)

security_expert = Agent(
    name="SecurityExpert",
    role="安全专家",
    goal="检查安全漏洞",
    tools=[check_security],
    llm=model
)

test_engineer = Agent(
    name="TestEngineer",
    role="测试工程师",
    goal="确保代码可测试性",
    tools=[run_tests],
    llm=model
)

senior_reviewer = Agent(
    name="SeniorReviewer",
    role="资深审查员",
    goal="综合所有审查意见，给出最终建议",
    llm=model
)

# 任务流程
def review_code(code: str):
    """审查代码"""
    
    # Task 1: 语法检查
    syntax_task = Task(
        description=f"检查以下代码的语法和格式:\n{code}",
        expected_output="语法检查报告",
        agent=syntax_checker
    )
    
    # Task 2-4: 并行审查
    logic_task = Task(
        description=f"审查代码逻辑:\n{code}",
        expected_output="逻辑审查报告",
        agent=logic_reviewer,
        async_execution=True
    )
    
    security_task = Task(
        description=f"检查安全问题:\n{code}",
        expected_output="安全检查报告",
        agent=security_expert,
        async_execution=True
    )
    
    test_task = Task(
        description=f"评估测试覆盖和可测试性:\n{code}",
        expected_output="测试评估报告",
        agent=test_engineer,
        async_execution=True
    )
    
    # Task 5: 综合审查
    final_review = Task(
        description="基于所有审查结果，给出最终的代码审查报告和改进建议",
        expected_output="完整的代码审查报告",
        agent=senior_reviewer,
        context=[syntax_task, logic_task, security_task, test_task]
    )
    
    # 创建团队
    crew = Crew(
        agents=[syntax_checker, logic_reviewer, security_expert, 
                test_engineer, senior_reviewer],
        tasks=[syntax_task, logic_task, security_task, test_task, final_review],
        process=Process.sequential,
        verbose=True
    )
    
    return crew.kickoff()

# 测试
if __name__ == "__main__":
    code_to_review = """
def calculate_total(items):
    total = 0
    for i in range(len(items)):
        total += items[i]['price'] * items[i]['quantity']
    return total
    """
    
    result = review_code(code_to_review)
    print("\n" + "="*50)
    print("代码审查结果:")
    print("="*50)
    print(result)
```

---

### 项目 2：内容创作工作流

```python
# 文件：deepagents_examples/project_content_creation.py

from deepagents import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 创作团队
researcher = Agent(
    name="Researcher",
    role="内容研究员",
    goal="深入研究主题，收集信息",
    backstory="资深研究员，擅长快速获取和整理信息",
    llm=model
)

writer = Agent(
    name="Writer",
    role="内容作家",
    goal="创作高质量的文章",
    backstory="经验丰富的作家，文笔优美，逻辑清晰",
    llm=model
)

editor = Agent(
    name="Editor",
    role="编辑",
    goal="完善文章质量",
    backstory="严格的编辑，注重细节和结构",
    llm=model
)

seo_specialist = Agent(
    name="SEOSpecialist",
    role="SEO 专家",
    goal="优化文章的 SEO 效果",
    backstory="熟悉 SEO 最佳实践，能够提升文章可见度",
    llm=model
)

def create_article(topic: str, keywords: list):
    """创作文章的完整流程"""
    
    # 研究
    research_task = Task(
        description=f"""
        研究主题：{topic}
        关键词：{', '.join(keywords)}
        
        请收集以下信息：
        1. 主题的核心概念
        2. 最新发展和趋势
        3. 相关案例和数据
        4. 可能的文章结构
        """,
        expected_output="详细的研究报告",
        agent=researcher
    )
    
    # 写作
    writing_task = Task(
        description="""
        基于研究报告，创作一篇文章：
        - 标题吸引人
        - 结构清晰（引言、正文、结论）
        - 包含具体例子
        - 长度 1500-2000 字
        """,
        expected_output="完整的文章初稿",
        agent=writer,
        context=[research_task]
    )
    
    # 编辑
    editing_task = Task(
        description="""
        编辑文章，改进：
        1. 语法和拼写
        2. 逻辑流畅性
        3. 段落结构
        4. 可读性
        """,
        expected_output="编辑后的文章",
        agent=editor,
        context=[writing_task]
    )
    
    # SEO 优化
    seo_task = Task(
        description=f"""
        优化文章的 SEO：
        1. 检查关键词密度：{', '.join(keywords)}
        2. 优化标题和副标题
        3. 添加 meta 描述
        4. 建议内部链接
        """,
        expected_output="SEO 优化后的最终文章和元数据",
        agent=seo_specialist,
        context=[editing_task]
    )
    
    # 创建团队
    crew = Crew(
        agents=[researcher, writer, editor, seo_specialist],
        tasks=[research_task, writing_task, editing_task, seo_task],
        process=Process.sequential,
        verbose=True
    )
    
    return crew.kickoff()

# 测试
if __name__ == "__main__":
    topic = "Python 异步编程最佳实践"
    keywords = ["async", "await", "asyncio", "异步编程", "Python"]
    
    result = create_article(topic, keywords)
    
    print("\n" + "="*60)
    print("最终文章:")
    print("="*60)
    print(result)
```

---

### 项目 3：数据分析 Pipeline

```python
# 文件：deepagents_examples/project_data_analysis.py

from deepagents import Agent, Task, Crew, Process
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# 数据工具
@tool
def load_data(source: str) -> str:
    """加载数据"""
    return f"数据已从 {source} 加载"

@tool
def clean_data(data_description: str) -> str:
    """清洗数据"""
    return "数据清洗完成: 移除了缺失值和异常值"

@tool
def analyze_statistics(data_description: str) -> str:
    """统计分析"""
    return "统计分析完成: 均值=42, 中位数=40, 标准差=5.2"

@tool
def create_visualization(chart_type: str) -> str:
    """创建可视化"""
    return f"已创建 {chart_type} 图表"

# 分析团队
data_engineer = Agent(
    name="DataEngineer",
    role="数据工程师",
    goal="加载和清洗数据",
    tools=[load_data, clean_data],
    llm=model
)

statistician = Agent(
    name="Statistician",
    role="统计分析师",
    goal="进行统计分析",
    tools=[analyze_statistics],
    llm=model
)

data_scientist = Agent(
    name="DataScientist",
    role="数据科学家",
    goal="深入分析数据模式和趋势",
    llm=model
)

visualizer = Agent(
    name="Visualizer",
    role="可视化专家",
    goal="创建数据可视化",
    tools=[create_visualization],
    llm=model
)

report_writer = Agent(
    name="ReportWriter",
    role="报告撰写员",
    goal="生成分析报告",
    llm=model
)

def analyze_data(data_source: str, analysis_goals: list):
    """完整的数据分析流程"""
    
    # Task 1: 数据准备
    prepare_task = Task(
        description=f"从 {data_source} 加载数据并进行清洗",
        expected_output="清洗后的数据描述",
        agent=data_engineer
    )
    
    # Task 2-3: 并行分析
    stats_task = Task(
        description="进行描述性统计分析",
        expected_output="统计分析结果",
        agent=statistician,
        context=[prepare_task],
        async_execution=True
    )
    
    pattern_task = Task(
        description=f"分析数据中的模式和趋势，重点关注: {', '.join(analysis_goals)}",
        expected_output="模式分析报告",
        agent=data_scientist,
        context=[prepare_task],
        async_execution=True
    )
    
    # Task 4: 可视化
    viz_task = Task(
        description="基于分析结果创建可视化图表",
        expected_output="可视化方案",
        agent=visualizer,
        context=[stats_task, pattern_task]
    )
    
    # Task 5: 报告
    report_task = Task(
        description="生成完整的数据分析报告",
        expected_output="最终分析报告",
        agent=report_writer,
        context=[stats_task, pattern_task, viz_task]
    )
    
    # 创建团队
    crew = Crew(
        agents=[data_engineer, statistician, data_scientist, 
                visualizer, report_writer],
        tasks=[prepare_task, stats_task, pattern_task, viz_task, report_task],
        process=Process.sequential,
        verbose=True
    )
    
    return crew.kickoff()

# 测试
if __name__ == "__main__":
    result = analyze_data(
        data_source="sales_data.csv",
        analysis_goals=["销售趋势", "季节性模式", "产品表现"]
    )
    
    print("\n" + "="*50)
    print("分析报告:")
    print("="*50)
    print(result)
```

---

## ✅ 最佳实践

### 1. Agent 设计原则

**DO（推荐）**：
```python
# ✅ 清晰的角色定义
agent = Agent(
    name="CodeReviewer",
    role="Python 代码审查专家",  # 具体的角色
    goal="发现代码问题并提供改进建议",  # 明确的目标
    backstory="10年Python开发经验，审查过1000+个项目",  # 丰富的背景
    llm=model
)
```

**DON'T（不推荐）**：
```python
# ❌ 模糊的定义
agent = Agent(
    name="Agent1",
    role="助手",  # 太宽泛
    goal="帮助用户",  # 不明确
    backstory="一个AI",  # 太简单
    llm=model
)
```

### 2. Task 设计原则

**DO（推荐）**：
```python
# ✅ 详细的任务描述
task = Task(
    description="""
    审查以下 Python 代码：
    {code}
    
    重点检查：
    1. 代码风格（PEP 8）
    2. 潜在的 bug
    3. 性能问题
    4. 安全漏洞
    
    对于每个问题，请说明：
    - 问题描述
    - 严重程度
    - 建议的修复方案
    """,
    expected_output="结构化的代码审查报告，包含问题列表和修复建议",
    agent=reviewer
)
```

**DON'T（不推荐）**：
```python
# ❌ 模糊的任务
task = Task(
    description="检查代码",  # 太简单
    expected_output="结果",  # 不明确
    agent=reviewer
)
```

### 3. 流程选择

| 场景 | 推荐流程 |
|------|----------|
| 独立任务，顺序执行 | Sequential |
| 需要管理和协调 | Hierarchical |
| 部分任务可并行 | Sequential + async_execution |
| 复杂自定义逻辑 | Custom Process |

### 4. 性能优化

```python
# 1. 使用异步任务
task1 = Task(description="...", agent=agent1, async_execution=True)
task2 = Task(description="...", agent=agent2, async_execution=True)

# 2. 合理使用缓存
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache

set_llm_cache(InMemoryCache())

# 3. 限制 Agent 迭代次数
agent = Agent(
    name="Agent",
    role="...",
    max_iter=5,  # 限制最大迭代
    llm=model
)

# 4. 批量处理
def process_batch(items):
    tasks = [create_task(item) for item in items]
    crew = Crew(agents=agents, tasks=tasks)
    return crew.kickoff()
```

### 5. 错误处理

```python
from deepagents import Crew

crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=True
)

try:
    result = crew.kickoff()
except Exception as e:
    print(f"执行失败: {str(e)}")
    # 记录错误
    # 重试或降级处理
```

---

## 📊 DeepAgents vs LangGraph

### 何时使用 DeepAgents？

✅ 适合：
- 多 Agent 协作场景
- 需要角色扮演的场景
- 任务分工明确
- 希望快速原型开发

### 何时使用 LangGraph？

✅ 适合：
- 需要精确控制状态流转
- 复杂的条件分支
- 需要检查点和恢复
- 对性能要求极高

### 组合使用

```python
# 在 DeepAgents Task 中使用 LangGraph
from langgraph.graph import StateGraph

def create_langgraph_tool():
    """创建基于 LangGraph 的工具"""
    graph = StateGraph(...)
    # 定义图结构
    return graph.compile()

# 作为工具提供给 Agent
agent = Agent(
    name="ComplexAgent",
    role="...",
    tools=[create_langgraph_tool()],
    llm=model
)
```

---

## 🎯 学习路线图

### 初级（1-2 周）
- [ ] 理解 Agent, Task, Crew 概念
- [ ] 创建简单的单 Agent 系统
- [ ] 使用工具
- [ ] 完成简单项目

### 中级（3-4 周）
- [ ] 多 Agent 协作
- [ ] 异步任务
- [ ] Hierarchical 模式
- [ ] 完成中等复杂度项目

### 高级（5-8 周）
- [ ] 自定义流程
- [ ] 高级记忆系统
- [ ] 性能优化
- [ ] 生产部署
- [ ] 完成大型项目

---

## 📚 参考资源

### 官方资源
- [DeepAgents GitHub](https://github.com/deepagents/deepagents)
- [DeepAgents 文档](https://docs.deepagents.ai)
- [示例项目](https://github.com/deepagents/examples)

### 社区资源
- Discord 社区
- GitHub Discussions
- Medium 文章

### 相关技术
- LangChain 基础
- LangGraph 状态图
- Prompt Engineering
- Multi-Agent Systems

---

**开始探索 DeepAgents 的强大功能！** 🚀
