from groq import Groq

import os


os.environ["GROQ_API_KEY"] = "ADD_YOUT_API_KEY"

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": "create a code that has 100 lines of code"
      }
    ],
    temperature=1,
    max_completion_tokens=10,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
