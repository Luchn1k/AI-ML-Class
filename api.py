from fastapi import FastAPI, Form
from chat_bot import chat


app = FastAPI()



@app.post("/chat")
def chat_with_bot(user_message: str = Form(...),user_name: str = Form(...) ):
    response = chat(user_name=user_name,
    message=user_message)
    return response


