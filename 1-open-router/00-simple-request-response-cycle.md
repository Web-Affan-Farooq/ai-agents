## Step:00  Simple request response cycle in openrouter 

Read these notes carefully to know what openrouter actually is [Link](https://github.com/panaversity/learn-agentic-ai/blob/main/01_ai_agents_first/02_openrouter/readme.md) . Then 

- Create account on [openrouter.ai](https://openrouter.ai/)
- On the left sidebar see option **API keys** . Give it a name , then copy and paste key not your .env file.

#### Setup a new project in uv
```bash
uv init && .venv\Scripts\activate
```
#### Install package :
```bash
uv add openai python-dotenv
```

after completing this step , navigate to the models section using top nav 

![models navigation](/images/model-nav.png)

Then search for your desired model 

![search model](/images//search.png)

Select model and copy it's name

![Example](/images/find-llm.png)

Make sure you're using free models for now . If you want to use paid models , then go to the profile and pay your credits . Openrouter costs you from your credits you've in your wallet and charge the desired amount on the basis of token requests per day . 

![credits](/images/credits.png)

Before using any paid model , make sure to checkout it's billing , ratings among other llms . Although usage of all paid and free llms are same . All llms are used as code below .

```python
## 1. ___ import libraries and packages
import os
from openai import OpenAI
from dotenv import load_dotenv

## 2. ___ Load and get envs
load_dotenv()
client_api_key = os.getenv("OPENROUTER_API_KEY") 

## 3. ___ Create an openai instance and use it for making requests
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", ## api url
    api_key=client_api_key, ## api key 
)

## 4. ___ Client usage ...
completion = client.chat.completions.create(
  model="deepseek/deepseek-r1-0528:free",  ## paste the model name you've copied ...
  messages=[
    {
        "role":"user",
        "content":"Hello . How are you"
    }
]
)
print('Chat response : ', completion) ## print complete returned response array not text 
```

run this file and check the result .
```bash
uv run main.py
```

And that's it .  Hope you'll find this guide helpful . If you want to create agents using openai agents sdk along with openrouter api , please check out the following guide [Link](./01-agent-openrouter-openaisdk.md)  