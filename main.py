import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")

st.title("AI Resume Critiquer 📄")
st.markdown("""
    Upload your resume in PDF format, and our AI will provide feedback on its content and structure.
""")  

openai_api_key = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are applying for:")

analyze = st.button("Analyze Resume")