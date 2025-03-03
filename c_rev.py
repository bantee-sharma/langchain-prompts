from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

chat_history = [
    SystemMessage(content="Hello! 😊 How can I assist you today?")
]

while True:
    user_input = input("yes: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))

    print("AI: ",res.content)
print(chat_history)