from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

hf_access_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
client = InferenceClient(api_key=hf_access_token)

st.header("summarization")
user_input = st.text_area("enter your text")

if st.button("summarize"):
    if user_input.strip():
        res = client.post(
            model = "facebook/bart-large-cnn",
            data = user_input
        )
        # Display the summary
        st.subheader("Summary:")
        st.write(res)  # Directly writing the response since it’s a string
    else:
        st.warning("Please enter some text to summarize!")