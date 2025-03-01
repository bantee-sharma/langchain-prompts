from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

hf_api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    huggingfacehub_api_token=hf_api_key
)

model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("you:")
    if user_input == 'exit':
        break
    result = model.invoke(user_input)

    print("AI:",result.content)