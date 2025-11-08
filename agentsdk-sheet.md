# Revision sheet for OpenAI Agents SDK :

### **Agent configuration :**
- For google colab

```python
import os
## ____ Importing google colab specific modules ...
import nest_asyncio
from google.colab import userdata

from agents import AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig
from rich import print
import asyncio

## ____ Make colab async ...
nest_asyncio.apply()
os.environ['GEMINI_API_KEY'] = userdata.get("GEMINI_API_KEY")
api_key = userdata.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True,
    )
```

### **Tool Calling :**
```python
from agents import function_tool

@function_tool
def example_tool():
    return "result of tool execution"

agent = Agent(
    name="example agent",
    instructions="system prompt",
    tools=[example_tool]
)
```

### **Context handling :**
```python
from agents import Agent , RunContextWrapper
from dataclasses import dataclass

@dataclass
class UserInfo:
    name:str,
    is_pro_user:bool

user_info = UserInfo(name="Affan", is_pro_user=True)

agent = Agent[UserInfo](
    name="Customer handling agent",
    instructions:"Use the tools"
)
```

### **Context and Dynamic Instructions :**
- `Information that is to be provided to llm` is called `context`
- Dynamic instructions is the process of `manipulating context in system prompt` .

```python
from agents import Agent , Runner , RunContextWrapper 
from dataclasses import dataclass 

@dataclass
class UserInfo:
  name:str
  is_pro_user:bool

user_info=UserInfo("Affan",True)

def dynamic_instructions(wrapper:RunContextWrapper[UserInfo], agent:Agent[UserInfo]) -> str:
  return f"Tell the user about his details , his name is {wrapper.context.name} and is pro user value is : {wrapper.context.is_pro_user}"

agent = Agent[UserInfo](
    name="Customer handling agent",
    instructions=dynamic_instructions,
)

async def main():
  result = await Runner.run(
      starting_agent=agent,
      input="Tell me wheather I'm a pro user or not",
      run_config=config,
      context=user_info
  )
  print(result.final_output)

asyncio.run(main())
```