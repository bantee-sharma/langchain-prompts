from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

print("🤖 Hey! I'm your AI buddy. Ask me anything! Type 'exit' or 'quit' whenever you're done chatting.")

prompt = PromptTemplate(
    template= '''You are a helpful and intelligent AI assistant. 
                 Answer the following question clearly and concisely.
                 User: {question}
                 Answer:''',
                 input_variables=["question"])

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.strip().lower() in["exit","quit"]:
        print("AI : Goodbye! Have a great day!")
        break
    else:
        chain = prompt | llm
        result = chain.invoke((chat_history))
        chat_history.append(AIMessage(content=result.content))
        print("AI: ",result.content)
print(chat_history)

