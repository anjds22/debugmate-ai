import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# ----------------------------
# Setup
# ----------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="DebugMate AI",
    page_icon="🐞",
    layout="centered"
)

st.title("🐞 DebugMate AI")
st.caption("Paste code + error → get instant fixes")

# ----------------------------
# Inputs
# ----------------------------
language = st.selectbox("Language", ["Python", "JavaScript", "Java", "C++"])

code = st.text_area("Your Code", height=200)

error = st.text_area("Error Message", height=150)

# ----------------------------
# Button
# ----------------------------
if st.button("🔍 Debug Now"):

    if not code.strip() or not error.strip():
        st.warning("Please paste both code and error.")
        st.stop()

    # ============================
    # ⚡ FAST LOCAL FIXES
    # ============================

    if "NameError" in error and "not defined" in error:
        st.markdown("""
## 🔍 What Went Wrong
You're using a variable that doesn't exist.

## 🧠 Why It Happened
Python doesn't know what the variable is yet.

## 🛠️ Fix
Define it first:

```python
name = "example"
print(name)