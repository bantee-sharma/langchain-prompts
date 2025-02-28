from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace,HuggingFacePipeline
from transformers import pipeline
from dotenv import load_dotenv
import streamlit as st
import os

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Integrate with LangChain
llm = HuggingFacePipeline(pipeline=summarizer)

# Summarize text
text = "Summarize the Word2Vec paper in 5 lines."
response = llm.invoke(text)

print(response)