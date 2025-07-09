## 01 Usage of openrouter combined with OpenAI agents SDK

In the previous guide, you've learned out how openrouter API works . Follow the steps below to create an AI agent using any free llm in openrouter and OpenAI agents SDK.

#### Step-1: 
Create uv project with virtual enviroment activated and install the following packages in it .

```bash
uv init . && .venv\Scripts\activate && uv add openai-agents python-dotenv
```

#### Step-2: 
Now we're going to create a clean configuration for connecting our agents to openrouter llms . Create a config.py file in root of the project and write configuration in it . Take help from the code below .

```python
## 1. ____ Import Libraries :
import os 
from dotenv import load_dotenv

## 2. ____ Import important classes :
from agents import AsyncOpenAI, OpenAIChatCompletionsModel , RunConfig

## 3. ____ Load all the enviroments Get api key ...
load_dotenv()
api_key = os.getenv("YOUR_OPENROUTER_API_KEY")

## 4. ____ Important : use AsyncOpenAI class for connecting with llm
client = AsyncOpenAI(
    api_key=api_key,  ## provide api key
    base_url="https://openrouter.ai/api/v1",  ## openrouter API url
)

## 5. ____ Important : Create model instance
model = OpenAIChatCompletionsModel(
      model="deepseek/deepseek-r1-0528:free", ## or any free llm you want to use . 
      openai_client=client, ## client created above for connecting to llm
)

## 6. ____ Create configuration ...
config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True ## Always true
)
```

### Step-3 :
Now in your main.py , create agent and run it using this custom configuration .

```python

from agents import Agent, Runner
from config import config ## import configuration from config.py

my_agent = Agent(
    name="Personal agent",
    instructions="You're my personal agent. I am testing your performance and working with deepseke R1"
)

result = Runner.run_sync(
    starting_agent=my_agent, input='Hello , please say Hello affan! .',run_config=config
)
print("Response : ",result.final_output)
```

And that's all , Here's how you'll be working on agents . This is the best approach for creating agents, both with free and paid llms . The main advantage for using llms in this manner is that you can't have to write different code for different llms . You can implement any feature of OpenAI agents SDK in this way .

## Importat note :
If you're using paid llms and you won't have enough credits in openrouter account , you'll likely recieve an error like this .

```bash
Traceback (most recent call last):
  File "E:\ai-agents\open-router\main.py", line 27, in <module>
    result = Runner.run_sync(
        starting_agent=my_agent, input='Hello , please send me a text message Hello affan! if you recieve this message .',run_config=config
    )
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\agents\run.py", line 252, in run_sync
    return runner.run_sync(
           ~~~~~~~~~~~~~~~^
        starting_agent,
        ^^^^^^^^^^^^^^^
    ...<5 lines>...
        previous_response_id=previous_response_id,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\agents\run.py", line 491, in run_sync
    return asyncio.get_event_loop().run_until_complete(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.run(
        ^^^^^^^^^
    ...<7 lines>...
        )
        ^
    )
    ^
  File "C:\Users\12345\AppData\Local\Programs\Python\Python313\Lib\asyncio\base_events.py", line 725, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\agents\run.py", line 397, in run
    input_guardrail_results, turn_result = await asyncio.gather(
                                           ^^^^^^^^^^^^^^^^^^^^^
    ...<19 lines>...
    )
    ^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\agents\run.py", line 910, in _run_single_turn
    new_response = await cls._get_new_response(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<11 lines>...
    )
    ^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\agents\run.py", line 1071, in _get_new_response
    new_response = await model.get_response(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<11 lines>...
    )
    ^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\agents\models\openai_chatcompletions.py", line 65, in get_response
    response = await self._fetch_response(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<10 lines>...
    )
    ^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\agents\models\openai_chatcompletions.py", line 273, in _fetch_response
    ret = await self._get_client().chat.completions.create(
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<20 lines>...
    )
    ^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\openai\resources\chat\completions\completions.py", line 2454, in create
    return await self._post(
           ^^^^^^^^^^^^^^^^^
    ...<45 lines>...
    )
    ^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\openai\_base_client.py", line 1784, in post
    return await self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\openai\_base_client.py", line 1584, in request
    raise self._make_status_error_from_response(err.response) from None
openai.APIStatusError: Error code: 402 - {'error': {'message': 'Insufficient credits. Add more using https://openrouter.ai/settings/credits', 'code': 402}}
```

Check this message in it 

```bash 
  File "E:\ai-agents\open-router\.venv\Lib\site-packages\openai\_base_client.py", line 1584, in request
    raise self._make_status_error_from_response(err.response) from None
openai.APIStatusError: Error code: 402 - {'error': {'message': 'Insufficient credits. Add more using https://openrouter.ai/settings/credits', 'code': 402}}
```