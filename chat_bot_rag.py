from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings 
from langchain_community.vectorstores import FAISS
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv(override=True)

book_agent_name = "aria"

Embedding_model = "nvidia/nemotron-3-embed-1b:free"
chunk_size = 1000
chunk_overlap= 200

top_k =2


vectorstores =  None



def create_rag(doc_name):
    global vectorstores
    print("starting rag creation")
    reader = PdfReader(f"docs/{doc_name}")
    number_of_pages = len(reader.pages)

    text = ""

    for i in range(1,number_of_pages):
        text = text + "\n\n"+ (reader.pages[i].extract_text())


    #split in to chunks
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_text(text)

    # for i in range(0,len(chunks)):
    #     print(chunks[i],"\n\n\n")


    # embeddings = OpenAIEmbeddings(
    #     model = Embedding_model,
    #     base_url= "https://openrouter.ai/api/v1/",
    #     api_key= os.getenv("OPENROUTER_API_KEY","")
    # )

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

    vectorstores = FAISS.from_texts(chunks,embeddings)
    print("end of rag creation")






max_tokens = 1024
def chat(message,user_name):
    
    llm = init_chat_model("openai/gpt-oss-120b", model_provider="groq", temperature=0.8, max_tokens= max_tokens)

    docs = vectorstores.similarity_search(message,top_k=top_k)

    context = "\n\n".join([doc.page_content for doc in docs])


    
    book_desc = f"""

        you are an librarian with over 15 years of experice, 
        
        your job is to answer users quections based on given context. 

        <context>
            {context}
        </context>


        Give your output in narnia slang. use context and how they speak in thir world. use any emoji if need. User's name is {user_name}
        use that name when you need

        Do not answer anything not related to given context. if asked give an answer in a creative way telling NO. Your allowd max tokens 
        to generate the output is {max_tokens}, try to be in that range.

        give the answer only. do not include your thinking. 

    
    """


    messages = [
        SystemMessage(content= book_desc),
        HumanMessage(content=message)
        ]
    

    response = llm.invoke(messages)
    return response.content




# 
# user_name = input("Enter your name : ")
# if user_name:
#     for i in range(10):
#         user_message = input("Enter your message : ")

#         if user_message == "q":
#             break

#         if user_message:

#             response = chat(user_message,user_name)
#             print(response)

#         else:
#             print("please enter a valid message")

# else:
#     print("enter a valid user name")













