from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model=  "gemini-1.5-pro")

msg = [
    SystemMessage(content = "you are a helpfull assitant"),
    HumanMessage(content = "tell me about langchain")
    ]

res = model.invoke(msg)

msg.append(AIMessage(content=res.content))

print(msg)