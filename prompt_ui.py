from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

st.header("summarization")

user_input = st.text_input("Enter your input")

if st.button("summarize"):
    
    res = model.invoke(user_input)

    st.write(res.content)