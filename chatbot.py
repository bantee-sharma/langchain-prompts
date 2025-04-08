from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

chat_history = [
    SystemMessage(content="You are a helpfull AI")
]

while True:
    input_text = input("You: ")
    chat_history.append(HumanMessage(content=input_text))
    if input_text == "exit":
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print("AI: ",res.content)
print(chat_history)

