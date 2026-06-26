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

st.set_page_config(
    page_title="DebugMate AI",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------
# Friendly UI Styling
# ----------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .card {
        background: #111827;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-size: 16px;
        font-weight: 600;
        background-color: #4F46E5;
        color: white;
    }

    .stTextArea textarea {
        font-family: monospace;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="main-title">🧠 DebugMate AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your friendly AI coding buddy that explains errors like a human tutor</div>', unsafe_allow_html=True)

st.divider()

# ----------------------------
# Layout
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("💻 Your Code")
    code = st.text_area(
        "",
        height=300,
        placeholder="Paste your code here..."
    )

with col2:
    st.subheader("❌ Error Message")
    error = st.text_area(
        "",
        height=300,
        placeholder="Paste the error / traceback here..."
    )

st.divider()

# ----------------------------
# Action
# ----------------------------
if st.button("🚀 Fix My Code"):

    if not code.strip() or not error.strip():
        st.warning("Please add both code and error message.")
    else:

        prompt = f"""
You are a friendly expert programming tutor.

Explain the error in a simple, beginner-friendly way.

Code:
{code}

Error:
{error}

Return format:

1. What went wrong (simple explanation)
2. Why it happened
3. How to fix it step-by-step
4. Corrected code
5. One pro tip
"""

        with st.spinner("Thinking like a senior engineer... 🧠"):
            response = model.generate_content(prompt)

        st.success("Done! Here's your fix 👇")

        st.markdown("### 🧾 Explanation")
        st.write(response.text)