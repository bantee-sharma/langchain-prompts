from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

chat_history = [
    SystemMessage(content="You are a helpfull assitant")
]

while True:
    user_input = input("Yes:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))

    print(res.content)
print(chat_history)