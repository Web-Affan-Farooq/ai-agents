from litellm import completion
import os 
from dotenv import load_dotenv

## 1. ____ Load and get enviroment variables ...
load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
responses = completion(
    model="gemini/gemini-2.5-flash",
    messages=[
        {
            "role":"user",
            "content":"Hello how are you!",
        }
    ]
)
for response in responses.choices:
     print("Response : ", response.message.content)