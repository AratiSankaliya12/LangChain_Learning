from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-5.2", temperature=0)

st.title("Chat with OpenAI's Chat Model")
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

template = load_prompt("template.json")

if st.button("Summarize"):
    user_input = template.format(
        paper=paper_input, style=style_input, length=length_input
    )
    result = model.invoke(user_input)
    st.write("Model Response:")
    st.write(result.content)
