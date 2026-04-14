import streamlit as st
from groq import Groq
import os

# ---- Groq Client ----
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ---- Page Config ----
st.set_page_config(
    page_title="Code Explainer AI",
    page_icon="🧠",
    layout="centered"
)

# ---- UI ----
st.title("🧠 Code Explainer AI")
st.markdown("Paste any code below and get a clear, plain-English explanation powered by AI.")

language = st.selectbox(
    "Select Programming Language",
    ["Python", "JavaScript", "Java", "C++", "SQL", "Other"]
)

code_input = st.text_area(
    "📋 Paste Your Code Here",
    height=250,
    placeholder="e.g. def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)"
)

if st.button("⚡ Explain Code"):
    if not code_input.strip():
        st.warning("Please paste some code first!")
    else:
        with st.spinner("Analyzing your code..."):
            prompt = f"""
You are an expert programming tutor. A beginner has shared the following {language} code.

Your job is to:
1. Give a short 1-2 line summary of what the code does
2. Explain it line by line in simple English
3. Mention any important concepts or patterns used (e.g. recursion, loops, API calls)
4. Point out any potential issues or improvements if any

Code:
{code_input}

Be beginner-friendly, clear, and structured.
"""
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            explanation = response.choices[0].message.content

        st.success("✅ Explanation Ready!")
        st.markdown("### 📖 Explanation")
        st.markdown(explanation)
