from langchain.chat_models import init_chat_model


llm = init_chat_model("openai/gpt-oss-120b", model_provider="groq", temperature=0,api_key = "ADD_YOUT_API_KEY", max_tokens= 1024)
response = llm.invoke("write a description about a hippo, 1000 words")
print(response.content)

print("\n\n\n","="*50,"\n\n\n")

llm = init_chat_model("openrouter/free", model_provider="openrouter", temperature=0,api_key = "ADD_YOUR_API_KEY", max_tokens= 1024)
response = llm.invoke("write a description about a hippo, 1000 words")
print(response.content)