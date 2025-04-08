from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

'''chat_history = [
    SystemMessage(content="Hello! 😊 How can I assist you today?")
]'''

memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)

conv = ConversationChain(
    llm=model,
    memory = memory
)

while True:
    user_input = input("yes: ")
    #chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    res = conv.invoke(user_input)
    #chat_history.append(AIMessage(content=res.content))

    print("AI: ",res.content)
