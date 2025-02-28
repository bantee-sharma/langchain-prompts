from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Define the HF model endpoint
llm = HuggingFaceEndpoint(
    repo_id="google/pegasus-xsum",
    task="summarization",
    huggingfacehub_api_token=api_key
)

# Summarization request
text = "The Eiffel Tower is 324 metres (1,063 ft) tall, making it the tallest structure in Paris. Built in 1889, it was the world’s tallest building until 1930."
response = llm.invoke(text)

print(response)
