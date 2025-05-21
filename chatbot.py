from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# Load environment variables from .env file (e.g., API keys)
load_dotenv()

# Initialize the Google Gemini model for chat
llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")


chat_history = [SystemMessage(content="You are a helpful and intelligent AI assistant.")]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.strip().lower() in ["exit","quit"]:
        print("AI: Goodbye! Have a great day!")
        break
    else:
        result = llm.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print("AI: ",result.content)
print(chat_history)
