# 文档索引

> 所有学习文档的完整清单和说明

## 📚 主要文档（按阅读顺序）

### 1. 入门文档

| 文件 | 说明 | 重要性 | 阅读时间 |
|------|------|--------|----------|
| `README.md` | 项目总览和导航 | ⭐⭐⭐ | 10分钟 |
| `QUICK_START.md` | 快速导航，选择学习路径 | 🚀🚀🚀 | 5分钟 |

### 2. 核心学习计划

| 文件 | 说明 | 重要性 | 学习时长 |
|------|------|--------|----------|
| `CURRICULUM_MASTER.md` | 60天精通计划主文档<br>包含 Week 1 (Day 1-7) 详细内容 | ⭐⭐⭐ | 1周 |
| `CURRICULUM_WEEK2-8.md` | Week 2-8 详细学习计划<br>Agent、LangGraph、DeepAgents、生产实践 | ⭐⭐⭐ | 7周 |
| `DEEPAGENTS_GUIDE.md` | DeepAgents 框架完全指南<br>包含教程、项目、最佳实践 | ⭐⭐⭐ | 2周 |

### 3. 原有文档（仍然有效）

| 文件 | 说明 | 重要性 | 备注 |
|------|------|--------|------|
| `CURRICULUM.md` | 原30天学习计划 | ⭐⭐ | 适合快速入门 |
| `CURRICULUM_30days_backup.md` | 30天计划备份 | ⭐ | 备份文件 |

### 4. 辅助文档

| 文件 | 说明 | 用途 |
|------|------|------|
| `UPDATE_SUMMARY.md` | 课程更新总结 | 了解更新内容 |
| `FILE_INDEX.md` | 本文档，文件索引 | 快速查找文档 |

---

## 📁 子目录文档

### learn-langchain/ 目录

#### 主要文档

| 文件路径 | 说明 | 重要性 |
|----------|------|--------|
| `learn-langchain/README.md` | 项目说明和快速开始 | ⭐⭐⭐ |
| `learn-langchain/ANTHROPIC_AGENT_README.md` | Anthropic Agent 完整指南 | ⭐⭐⭐ |
| `learn-langchain/FILE_STRUCTURE.md` | 详细的文件结构说明 | ⭐⭐ |

#### 使用指南（guides/）

| 文件路径 | 说明 | 重要性 |
|----------|------|--------|
| `docs/guides/ENV_CONFIG_GUIDE.md` | 环境配置和 API Keys | ⭐⭐⭐ |
| `docs/guides/WEATHER_API_GUIDE.md` | 外部 API 集成示例 | ⭐⭐ |
| `docs/guides/HOW_TO_FILL_USER_INFO.md` | 生产环境最佳实践 | ⭐⭐⭐ |

#### 进阶文档（advanced/）

| 文件路径 | 说明 | 重要性 |
|----------|------|--------|
| `docs/advanced/create-agent-analysis.md` | create_agent 源码分析 | ⭐⭐⭐ |
| `docs/advanced/tool-strategy-analysis.md` | ToolStrategy 原理解析 | ⭐⭐⭐ |
| `docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md` | AgentState 详解 | ⭐⭐⭐ |

#### 示例代码（examples/）

| 类型 | 文件 | 说明 |
|------|------|------|
| **入门示例** | `use-agent-anthropic-qa-only.py` | 最简单的问答（⭐推荐新手） |
| | `use-agent-anthropic-simple.py` | 带工具的Agent |
| | `use-agent-anthropic-langgraph.py` | LangGraph版本 |
| **工具集成** | `use-agent-tool.py` | 基础工具创建 |
| | `use-agent-tool-real-weather.py` | 真实API集成 |
| **记忆管理** | `use-agent-with-memory-1.py` | 基础记忆 |
| | `use-agent-with-memory-improved.py` | 改进版本 |
| | `use-agent-with-memory-realistic.py` | 生产级实现（⭐重点） |
| **测试工具** | `test-anthropic-agent.py` | 配置验证 |
| | `compare-state-fields.py` | State结构对比 |

---

## 🗂️ 按学习阶段分类

### 阶段 1：入门（Day 1-7）

**必读文档**：
1. `README.md` - 项目总览
2. `QUICK_START.md` - 快速导航
3. `CURRICULUM_MASTER.md` - Week 1 内容
4. `learn-langchain/README.md` - 项目说明
5. `learn-langchain/docs/guides/ENV_CONFIG_GUIDE.md` - 环境配置

**参考文档**：
- `learn-langchain/ANTHROPIC_AGENT_README.md`
- `CURRICULUM.md`（原30天计划）

**示例代码**：
- `examples/use-agent-anthropic-qa-only.py`
- `examples/use-agent-anthropic-simple.py`

---

### 阶段 2：Agent 和 Tools（Day 8-14）

**必读文档**：
1. `CURRICULUM_WEEK2-8.md` - Week 2 内容

**参考文档**：
- `learn-langchain/docs/guides/WEATHER_API_GUIDE.md`
- `learn-langchain/docs/guides/HOW_TO_FILL_USER_INFO.md`
- `learn-langchain/docs/advanced/create-agent-analysis.md`
- `learn-langchain/docs/advanced/tool-strategy-analysis.md`

**示例代码**：
- `examples/use-agent-tool.py`
- `examples/use-agent-tool-real-weather.py`
- `examples/use-agent-with-memory-*.py`

---

### 阶段 3：LangGraph（Day 15-28）

**必读文档**：
1. `CURRICULUM_WEEK2-8.md` - Week 3-4 内容

**参考文档**：
- `learn-langchain/docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md`

**示例代码**：
- `examples/use-agent-anthropic-langgraph.py`
- `examples/compare-state-fields.py`

---

### 阶段 4：DeepAgents（Day 29-42）

**必读文档**：
1. `DEEPAGENTS_GUIDE.md` - 完全指南 ⭐⭐⭐
2. `CURRICULUM_WEEK2-8.md` - Week 5-6 内容

**参考文档**：
- DeepAgents 官方文档
- `deepagents/` 目录下的源码

---

### 阶段 5：生产实践（Day 43-60）

**必读文档**：
1. `CURRICULUM_WEEK2-8.md` - Week 7-8 内容

**参考文档**：
- `learn-langchain/docs/guides/HOW_TO_FILL_USER_INFO.md`
- 所有进阶文档（`docs/advanced/`）

---

## 🔍 按主题查找文档

### 环境配置
- `README.md` - 快速开始部分
- `learn-langchain/docs/guides/ENV_CONFIG_GUIDE.md`

### LangChain 基础
- `CURRICULUM_MASTER.md` - Week 1
- `learn-langchain/ANTHROPIC_AGENT_README.md`

### Agent 开发
- `CURRICULUM_WEEK2-8.md` - Week 2
- `learn-langchain/docs/advanced/create-agent-analysis.md`

### LangGraph
- `CURRICULUM_WEEK2-8.md` - Week 3-4
- `learn-langchain/docs/advanced/AGENT_STATE_FIELDS_EXPLAINED.md`

### DeepAgents
- `DEEPAGENTS_GUIDE.md` ⭐⭐⭐

### 生产实践
- `CURRICULUM_WEEK2-8.md` - Week 7-8
- `learn-langchain/docs/guides/HOW_TO_FILL_USER_INFO.md`

### 工具和 API
- `CURRICULUM_WEEK2-8.md` - Week 2
- `learn-langchain/docs/guides/WEATHER_API_GUIDE.md`

### 记忆管理
- `CURRICULUM_WEEK2-8.md` - Week 2 Day 12
- `examples/use-agent-with-memory-*.py`

### 性能优化
- `CURRICULUM_WEEK2-8.md` - Week 7

### 部署维护
- `CURRICULUM_WEEK2-8.md` - Week 8

---

## 📊 文档统计

### 主要文档
- 入门文档：2 个
- 核心学习计划：3 个
- 原有文档：2 个
- 辅助文档：2 个

### learn-langchain/ 子目录
- 主要文档：3 个
- 使用指南：3 个
- 进阶文档：3 个
- 示例代码：10 个

**总计**：28 个文档和代码文件

---

## 💡 使用建议

1. **新手**：
   - 先看 `QUICK_START.md`
   - 然后按 `CURRICULUM_MASTER.md` 学习

2. **有基础**：
   - 直接看 `CURRICULUM_WEEK2-8.md`
   - 重点学习感兴趣的部分

3. **查找特定主题**：
   - 使用"按主题查找文档"部分
   - 用 Ctrl+F 搜索关键词

4. **遇到问题**：
   - 先查看相关文档
   - 再看示例代码
   - 最后查官方文档或提问

---

*文档索引 - 最后更新: 2026-03-04*
