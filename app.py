import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()
genai.configure(api_key=os.getenv("AQ.Ab8RN6KaZMGsrWUcd9gha5CMdwa60P0_fIgm_47GFRxlitsy4w"))
model = genai.GenerativeModel("models/gemini-2.0-flash")

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="DebugMate AI",
    page_icon="🐞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0d0f1a !important;
    color: #e2e4f0 !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stAppViewContainer"] > .main {
    background: #0d0f1a !important;
}

[data-testid="stSidebar"] {
    background: #11131f !important;
    border-right: 1px solid #1e2035 !important;
}

[data-testid="stSidebar"] * {
    color: #e2e4f0 !important;
}

.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0.25rem 0 1.25rem 0;
}

.sidebar-brand-icon {
    width: 38px;
    height: 38px;
    background: linear-gradient(135deg, #6c63ff, #4f46e5);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    box-shadow: 0 4px 14px rgba(108, 99, 255, 0.4);
}

.sidebar-brand-text {
    font-size: 18px;
    font-weight: 700;
    background: linear-gradient(90deg, #a5b4fc, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.error-chip {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: #181a2e;
    border: 1px solid #252848;
    border-radius: 8px;
    margin-bottom: 6px;
    font-size: 13px;
    font-family: 'JetBrains Mono', monospace;
    color: #a5b4fc !important;
    font-weight: 500;
}

.error-chip .dot {
    width: 7px;
    height: 7px;
    background: #4ade80;
    border-radius: 50%;
    flex-shrink: 0;
    box-shadow: 0 0 6px rgba(74, 222, 128, 0.6);
}

.sidebar-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4b5280 !important;
    margin: 1rem 0 0.5rem 0;
}

.tech-stack {
    background: #181a2e;
    border: 1px solid #1e2035;
    border-radius: 10px;
    padding: 12px 14px;
    margin-top: 0.5rem;
}

.tech-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12.5px;
    color: #8b92b8 !important;
    padding: 3px 0;
}

.tech-dot {
    width: 5px;
    height: 5px;
    background: #6c63ff;
    border-radius: 50%;
}

.hero-section {
    text-align: center;
    padding: 2rem 0 1.5rem 0;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(108, 99, 255, 0.12);
    border: 1px solid rgba(108, 99, 255, 0.3);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 12px;
    font-weight: 600;
    color: #a5b4fc;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.hero-title {
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 60%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.6rem 0;
}

.hero-sub {
    font-size: 15px;
    color: #5c6391;
    font-weight: 400;
    max-width: 440px;
    margin: 0 auto;
    line-height: 1.6;
}

.custom-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #1e2035, transparent);
    margin: 1.5rem 0;
}

.card {
    background: #11131f;
    border: 1px solid #1a1d30;
    border-radius: 14px;
    padding: 1.25rem 1.25rem 0.75rem 1.25rem;
    height: 100%;
}

.card-label {
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #4b5280;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 6px;
}

.stTextArea textarea {
    background: #0d0f1a !important;
    color: #c8cde8 !important;
    border: 1px solid #1e2035 !important;
    border-radius: 10px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13.5px !important;
    line-height: 1.65 !important;
    padding: 14px !important;
    transition: border-color 0.2s ease !important;
    resize: vertical !important;
}

.stTextArea textarea:focus {
    border-color: #6c63ff !important;
    box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.12) !important;
    outline: none !important;
}

.stTextArea textarea::placeholder {
    color: #2e3252 !important;
}

.stTextArea label { display: none !important; }

.stSelectbox > div > div {
    background: #0d0f1a !important;
    border: 1px solid #1e2035 !important;
    border-radius: 10px !important;
    color: #c8cde8 !important;
    font-size: 14px !important;
}

.stSelectbox label { display: none !important; }

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #6c63ff 0%, #4f46e5 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    height: 52px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(108, 99, 255, 0.35) !important;
    font-family: 'Inter', sans-serif !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 28px rgba(108, 99, 255, 0.5) !important;
    background: linear-gradient(135deg, #7c73ff 0%, #5f56f5 100%) !important;
}

.stButton > button:active {
    transform: translateY(0px) !important;
}

.stWarning {
    background: rgba(251, 191, 36, 0.08) !important;
    border: 1px solid rgba(251, 191, 36, 0.2) !important;
    border-radius: 10px !important;
    color: #fbbf24 !important;
}

.result-card {
    background: #11131f;
    border: 1px solid #1a1d30;
    border-radius: 16px;
    padding: 2rem 2rem 1.5rem 2rem;
    margin-top: 1.5rem;
    position: relative;
    overflow: hidden;
}

.result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #6c63ff, #4ade80, #6c63ff);
}

.result-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 1.25rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #1a1d30;
}

.result-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(74, 222, 128, 0.1);
    border: 1px solid rgba(74, 222, 128, 0.25);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: 600;
    color: #4ade80;
}

[data-testid="column"] { padding: 0 0.5rem !important; }

.block-container {
    padding: 1.5rem 2rem 3rem 2rem !important;
    max-width: 1200px !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none !important; }

.lang-label {
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #4b5280;
    margin-bottom: 0.4rem;
    display: flex;
    align-items: center;
    gap: 6px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-icon">🐞</div>
        <div class="sidebar-brand-text">DebugMate AI</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">Supported Errors</div>', unsafe_allow_html=True)

    errors = [
        "NameError", "TypeError", "SyntaxError", "IndexError",
        "ModuleNotFoundError", "FileNotFoundError", "AttributeError", "ValueError",
    ]
    for err in errors:
        st.markdown(f'<div class="error-chip"><span class="dot"></span>{err}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label" style="margin-top:1.5rem;">Powered by</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tech-stack">
        <div class="tech-item"><span class="tech-dot"></span>Google Gemini 2.0 Flash</div>
        <div class="tech-item"><span class="tech-dot"></span>Python 3.x</div>
        <div class="tech-item"><span class="tech-dot"></span>Streamlit</div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# Hero Header
# ----------------------------
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">🐞 AI Debugger</div>
    <div class="hero-title">Fix bugs instantly</div>
    <div class="hero-sub">Paste your code and error — get a clear, beginner-friendly explanation and fix in seconds.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# ----------------------------
# Input Layout
# ----------------------------
left, right = st.columns(2, gap="medium")

with left:
    st.markdown('<div class="card-label">⌨️ &nbsp;Your Code</div>', unsafe_allow_html=True)
    st.markdown('<div class="lang-label">🌐 &nbsp;Language</div>', unsafe_allow_html=True)
    language = st.selectbox("lang", ["Python", "JavaScript", "Java", "C++"], label_visibility="collapsed")
    code = st.text_area(
        "code_input",
        height=340,
        placeholder="# Paste your Python code here...\n\ndef greet(name):\n    print('Hello, ' + name)\n\ngreet(42)",
        label_visibility="collapsed"
    )

with right:
    st.markdown('<div class="card-label">❌ &nbsp;Error Message</div>', unsafe_allow_html=True)
    st.markdown('<div style="height: 57px;"></div>', unsafe_allow_html=True)
    error = st.text_area(
        "error_input",
        height=340,
        placeholder="Traceback (most recent call last):\n  File \"main.py\", line 5, in <module>\n    greet(42)\nTypeError: can only concatenate str (not \"int\") to str",
        label_visibility="collapsed"
    )

# ----------------------------
# Analyze Button
# ----------------------------
st.markdown('<div style="margin-top: 1.25rem;">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze = st.button("🔍  Analyze & Fix My Code")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Analysis Logic
# ----------------------------
if analyze:
    if code.strip() == "" or error.strip() == "":
        st.warning("⚠️  Please provide both your code and the error message before analyzing.")
    else:
        prompt = f"""
You are an expert programming tutor helping a beginner understand and fix their code.

Programming language: {language}

Code:
{code}

Error:
{error}

Respond using this exact format with clear markdown headings:

## 🔍 What Went Wrong
A plain-English explanation of the error (1–2 sentences, no jargon).

## 🧠 Why It Happened
A brief, friendly explanation of the root cause.

## 🛠️ Step-by-Step Fix
Numbered steps explaining what to change and why.

## ✅ Corrected Code
The full corrected code in a code block.

## 💡 Tips to Avoid This
2–3 practical habits or rules to avoid this error in the future.

Keep the tone encouraging and beginner-friendly. Use simple analogies where helpful.
"""
        st.markdown("""
        <div class="result-card">
            <div class="result-header">
                <div class="result-badge">✓ Analysis Complete</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.spinner("Analyzing your code..."):
            response = model.generate_content(prompt, stream=True)

        output = st.empty()
        full_text = ""
        for chunk in response:
            if chunk.text:
                full_text += chunk.text
                output.markdown(full_text)