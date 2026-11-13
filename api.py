from fastapi import FastAPI, Form
from chat_bot_rag import chat,create_rag
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI): 
    create_rag("10_fantasy_books_guide.pdf")
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/chat")
def chat_with_bot(user_message: str = Form(...),user_name: str = Form(...) ):
    response = chat(user_name=user_name,
    message=user_message)
    return response


