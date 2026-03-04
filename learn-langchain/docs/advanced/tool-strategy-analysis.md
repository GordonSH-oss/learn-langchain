# `ToolStrategy` 工作原理分析

## 📋 概述

`ToolStrategy` 是 LangChain Agents 中用于实现结构化输出的策略之一。它通过**工具调用（Tool Calling）**的方式，让模型返回符合指定 schema 的结构化数据。

## 🎯 核心思想

`ToolStrategy` 的核心思想是：
1. **将 schema 转换为工具**：将 Pydantic 模型、dataclass、TypedDict 或 JSON schema 转换为一个"虚拟工具"
2. **模型调用工具**：模型通过 tool_calls 返回结构化数据
3. **解析工具参数**：从 tool_call 的 args 中解析出符合 schema 的结构化数据

## 🔧 类结构分析

### ToolStrategy 类定义

```python
@dataclass(init=False)
class ToolStrategy(Generic[SchemaT]):
    """Use a tool calling strategy for model responses."""
    
    schema: type[SchemaT]
    """Schema for the tool calls."""
    
    schema_specs: list[_SchemaSpec[SchemaT]]
    """Schema specs for the tool calls."""
    
    tool_message_content: str | None
    """The content of the tool message to be returned when the model calls
    an artificial structured output tool."""
    
    handle_errors: bool | str | type[Exception] | ...
    """Error handling strategy for structured output via ToolStrategy."""
```

### 关键属性说明

1. **`schema`**: 用户提供的 schema（Pydantic 模型、dataclass、TypedDict 或 JSON schema）
2. **`schema_specs`**: 从 schema 解析出的规范列表（支持 Union 类型，会拆分为多个 specs）
3. **`tool_message_content`**: 当模型调用结构化输出工具时，返回的 tool message 内容
4. **`handle_errors`**: 错误处理策略

## 🔄 完整工作流程

### 第一阶段：初始化（在 `create_agent` 中）

#### 1. 创建 ToolStrategy 实例

```python
# 用户传入 schema
response_format = ToolStrategy(schema=MyPydanticModel)

# 或者在 create_agent 中自动转换
if isinstance(response_format, AutoStrategy):
    tool_strategy_for_setup = ToolStrategy(schema=response_format.schema)
```

#### 2. 解析 Schema Specs

```python
# ToolStrategy.__init__ 中会解析 schema
def _iter_variants(schema: Any) -> Iterable[Any]:
    """Yield leaf variants from Union and JSON Schema oneOf."""
    if get_origin(schema) in (UnionType, Union):
        for arg in get_args(schema):
            yield from _iter_variants(arg)
        return
    # ... 处理其他情况
    yield schema

self.schema_specs = [_SchemaSpec(s) for s in _iter_variants(schema)]
```

**关键点：**
- 支持 Union 类型，会拆分为多个独立的 schema specs
- 每个 schema spec 包含：schema、name、description、schema_kind、json_schema

#### 3. 创建结构化输出工具绑定

```python
structured_output_tools: dict[str, OutputToolBinding] = {}
if tool_strategy_for_setup:
    for response_schema in tool_strategy_for_setup.schema_specs:
        structured_tool_info = OutputToolBinding.from_schema_spec(response_schema)
        structured_output_tools[structured_tool_info.tool.name] = structured_tool_info
```

**OutputToolBinding 的作用：**
- 将 schema spec 转换为一个 `StructuredTool` 实例
- 这个工具会被绑定到模型上，模型可以"调用"它
- 工具的名称通常是 schema 的类名

### 第二阶段：模型绑定（在 `_get_bound_model` 中）

```python
def _get_bound_model(request: ModelRequest) -> tuple[Runnable, ResponseFormat | None]:
    # ...
    
    # 如果使用 ToolStrategy，将结构化输出工具添加到工具列表
    final_tools = list(request.tools)
    if isinstance(effective_response_format, ToolStrategy):
        # 添加结构化输出工具
        structured_tools = [info.tool for info in structured_output_tools.values()]
        final_tools.extend(structured_tools)
    
    # 绑定工具到模型
    if isinstance(effective_response_format, ToolStrategy):
        # 强制使用工具（如果有结构化输出工具）
        tool_choice = "any" if structured_output_tools else request.tool_choice
        return (
            request.model.bind_tools(
                final_tools, tool_choice=tool_choice, **request.model_settings
            ),
            effective_response_format,
        )
```

**关键点：**
- 结构化输出工具被添加到模型的工具列表中
- 如果存在结构化输出工具，`tool_choice` 会被设置为 `"any"`，强制模型使用工具

### 第三阶段：模型执行和输出处理（在 `_handle_model_output` 中）

```python
def _handle_model_output(
    output: AIMessage, effective_response_format: ResponseFormat | None
) -> dict[str, Any]:
    # ...
    
    # 处理 ToolStrategy 的结构化输出
    if (
        isinstance(effective_response_format, ToolStrategy)
        and isinstance(output, AIMessage)
        and output.tool_calls
    ):
        # 1. 找出结构化输出工具调用
        structured_tool_calls = [
            tc for tc in output.tool_calls 
            if tc["name"] in structured_output_tools
        ]
        
        if structured_tool_calls:
            # 2. 检查是否有多个结构化输出（错误情况）
            if len(structured_tool_calls) > 1:
                exception = MultipleStructuredOutputsError(...)
                should_retry, error_message = _handle_structured_output_error(...)
                if not should_retry:
                    raise exception
                # 返回错误消息，让模型重试
                return {"messages": [output, *tool_messages]}
            
            # 3. 处理单个结构化输出
            tool_call = structured_tool_calls[0]
            try:
                # 解析工具参数
                structured_tool_binding = structured_output_tools[tool_call["name"]]
                structured_response = structured_tool_binding.parse(tool_call["args"])
                
                # 创建 tool message
                tool_message_content = (
                    effective_response_format.tool_message_content
                    if effective_response_format.tool_message_content
                    else f"Returning structured response: {structured_response}"
                )
                
                return {
                    "messages": [
                        output,
                        ToolMessage(
                            content=tool_message_content,
                            tool_call_id=tool_call["id"],
                            name=tool_call["name"],
                        ),
                    ],
                    "structured_response": structured_response,  # 关键：返回解析后的结构化数据
                }
            except Exception as exc:
                # 处理解析错误
                exception = StructuredOutputValidationError(...)
                should_retry, error_message = _handle_structured_output_error(...)
                if not should_retry:
                    raise exception
                # 返回错误消息，让模型重试
                return {"messages": [output, *tool_messages]}
    
    return {"messages": [output]}
```

**关键步骤：**
1. **识别结构化输出工具调用**：从 `output.tool_calls` 中找出属于结构化输出的工具调用
2. **验证**：确保只有一个结构化输出工具调用（多个会报错）
3. **解析**：使用 `OutputToolBinding.parse()` 解析工具参数
4. **返回**：返回解析后的结构化数据（`structured_response`）和 tool message

### 第四阶段：解析工具参数（在 `OutputToolBinding.parse` 中）

```python
def parse(self, tool_args: dict[str, Any]) -> SchemaT:
    """Parse tool arguments according to the schema."""
    return _parse_with_schema(self.schema, self.schema_kind, tool_args)
```

**`_parse_with_schema` 函数：**
```python
def _parse_with_schema(
    schema: type[SchemaT] | dict, 
    schema_kind: SchemaKind, 
    data: dict[str, Any]
) -> Any:
    if schema_kind == "json_schema":
        return data
    try:
        adapter: TypeAdapter[SchemaT] = TypeAdapter(schema)
        return adapter.validate_python(data)
    except Exception as e:
        # 处理解析错误
        ...
```

**支持的 Schema 类型：**
- **Pydantic 模型**：使用 `TypeAdapter` 验证
- **dataclass**：使用 `TypeAdapter` 验证
- **TypedDict**：使用 `TypeAdapter` 验证
- **JSON schema dict**：直接返回数据

### 第五阶段：图路由处理（在条件边中）

#### 1. Model → Tools 路由

```python
def _make_model_to_tools_edge(...):
    def model_to_tools(state: dict[str, Any]) -> str | list[Send] | None:
        # ...
        
        # 检查是否有待处理的工具调用
        pending_tool_calls = [
            c for c in last_ai_message.tool_calls
            if c["id"] not in tool_message_ids 
            and c["name"] not in structured_output_tools  # 关键：排除结构化输出工具
        ]
        
        # 如果有待处理的工具调用，跳转到 tools 节点
        if pending_tool_calls:
            return ["tools"]
        
        # 如果有结构化输出工具调用，直接结束（不执行实际工具）
        if any(tc["name"] in structured_output_tools for tc in last_ai_message.tool_calls):
            return end_destination
        
        # 否则继续循环
        return model_destination
```

**关键点：**
- 结构化输出工具调用**不会**被路由到 `tools` 节点执行
- 它们会在 `_handle_model_output` 中被处理
- 如果有结构化输出工具调用，可以直接结束（返回 `end_destination`）

#### 2. Tools → Model 路由

```python
def _make_tools_to_model_edge(...):
    def tools_to_model(state: dict[str, Any]) -> str | None:
        # ...
        
        # 如果执行了结构化输出工具，直接结束
        if any(t.name in structured_output_tools for t in tool_messages):
            return end_destination
        
        # 否则继续循环
        return model_destination
```

## 📊 完整流程图

```
用户定义 Schema
    ↓
创建 ToolStrategy(schema=...)
    ↓
解析为 SchemaSpecs（支持 Union）
    ↓
创建 OutputToolBinding（转换为 StructuredTool）
    ↓
添加到模型的工具列表
    ↓
模型执行，返回 tool_calls
    ↓
识别结构化输出工具调用
    ↓
解析 tool_call["args"]
    ↓
验证并转换为 Schema 实例
    ↓
返回 structured_response
```

## 💡 关键设计特点

### 1. 兼容性
- **不依赖模型原生支持**：即使模型不支持原生结构化输出（如 ProviderStrategy），也可以使用 ToolStrategy
- **通用性**：适用于所有支持工具调用的模型

### 2. 灵活性
- **支持多种 Schema 类型**：Pydantic、dataclass、TypedDict、JSON schema
- **支持 Union 类型**：可以定义多个可能的输出格式
- **错误处理**：支持多种错误处理策略（重试、自定义消息等）

### 3. 与普通工具的区别
- **不实际执行**：结构化输出工具不会真正执行，只是用来传递结构化数据
- **特殊路由**：在图中会被特殊处理，不会路由到 `tools` 节点
- **直接解析**：从 `tool_call["args"]` 中直接解析，不需要等待工具执行结果

## 🔍 示例场景

### 场景 1：简单结构化输出

```python
from pydantic import BaseModel
from langchain.agents import create_agent, ToolStrategy

class WeatherResponse(BaseModel):
    location: str
    temperature: float
    condition: str

agent = create_agent(
    model="openai:gpt-4",
    response_format=ToolStrategy(schema=WeatherResponse)
)

# 模型会调用一个名为 "WeatherResponse" 的工具
# tool_call = {
#     "name": "WeatherResponse",
#     "args": {"location": "Tokyo", "temperature": 25.0, "condition": "sunny"}
# }
# 然后解析为 WeatherResponse 实例
```

### 场景 2：Union 类型

```python
from typing import Union

class SuccessResponse(BaseModel):
    status: str = "success"
    data: dict

class ErrorResponse(BaseModel):
    status: str = "error"
    message: str

agent = create_agent(
    model="openai:gpt-4",
    response_format=ToolStrategy(schema=Union[SuccessResponse, ErrorResponse])
)

# 会创建两个工具：SuccessResponse 和 ErrorResponse
# 模型可以选择调用其中一个
```

### 场景 3：自定义错误处理

```python
agent = create_agent(
    model="openai:gpt-4",
    response_format=ToolStrategy(
        schema=WeatherResponse,
        handle_errors="Please provide valid weather data",
        tool_message_content="Weather data received"
    )
)
```

## 🆚 ToolStrategy vs ProviderStrategy

| 特性 | ToolStrategy | ProviderStrategy |
|------|-------------|------------------|
| **实现方式** | 工具调用 | 模型原生支持 |
| **兼容性** | 所有支持工具调用的模型 | 仅支持原生结构化输出的模型 |
| **性能** | 需要额外的工具调用步骤 | 直接返回结构化数据 |
| **灵活性** | 高（支持 Union、自定义错误处理） | 中（依赖模型能力） |
| **使用场景** | 通用场景，需要兼容性 | 模型原生支持时优先使用 |

## 📝 总结

`ToolStrategy` 通过以下机制实现结构化输出：

1. **Schema → Tool 转换**：将 schema 转换为虚拟工具
2. **模型调用工具**：模型通过 tool_calls 返回结构化数据
3. **参数解析**：从 tool_call["args"] 中解析并验证数据
4. **特殊路由**：在图中特殊处理，不执行实际工具

这种设计的优势是：
- ✅ 兼容性好，适用于所有支持工具调用的模型
- ✅ 灵活性强，支持多种 schema 类型和错误处理策略
- ✅ 与现有工具调用机制无缝集成

缺点是：
- ❌ 需要额外的工具调用步骤，可能略微影响性能
- ❌ 依赖模型的工具调用能力

