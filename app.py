import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

st.set_page_config(
    page_title="DebugMate AI",
    page_icon="🐞",
    layout="wide"
)

st.title("🐞 DebugMate AI")
st.caption("Paste your code and error message to get instant debugging help.")

language = st.selectbox(
    "Programming Language",
    ["Python"]
)

code = st.text_area(
    "Paste your code",
    height=250
)

error = st.text_area(
    "Paste the error message",
    height=150
)

if st.button("🔍 Debug"):
    # your Gemini code here

        prompt = f"""
You are an expert programming tutor.

Programming language: {language}

Code:
{code}

Error:
{error}

Respond using this format:

1. Error explanation
2. Why it happened
3. Step-by-step fix
4. Corrected code
5. Tips to avoid this error in the future

Keep explanations beginner-friendly.
"""

        response = model.generate_content(prompt)

        st.markdown(response.text)