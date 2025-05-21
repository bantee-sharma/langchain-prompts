from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# Load environment variables from .env file (e.g., API keys)
load_dotenv()

# Initialize the Google Gemini model for chat
llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

# Initialize chat history with a system message that sets AI's role and behavior
chat_history = [SystemMessage(content="You are a helpful and intelligent AI assistant.")]


print("🤖 Hey! I'm your AI buddy. Ask me anything! Type 'exit' or 'quit' to end.")

while True:
    # Get user input
    user_input = input("You: ")
    # Append user's message to chat history
    chat_history.append(HumanMessage(content=user_input))
    # Check if the user wants to exit the chat
    if user_input.strip().lower() in ["exit","quit"]:
        print("AI: Goodbye! Have a great day!")
        break # Exit the while loop to end program
    else:
        # Send entire conversation history to the LLM to generate a response
        result = llm.invoke(chat_history)
        # Append AI's response to chat history to maintain context for next turn
        chat_history.append(AIMessage(content=result.content))
        # Display the AI's response
        print("AI: ",result.content)
print(chat_history)
