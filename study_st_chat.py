import streamlit as st
from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools
from agno.tools.youtube import YouTubeTools

load_dotenv()

st.set_page_config(page_title="Studyfetch Chat", page_icon="📚", layout="wide")
st.title("📚 Studyfetch- Your AI Study Partner")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Sidebar for API key status
def api_key_status():
    exa_key = os.getenv("EXA_API_KEY")
    if exa_key:
        st.sidebar.success("EXA API Key loaded.")
    else:
        st.sidebar.warning("EXA API Key not found!")
api_key_status()

# Agent setup
def get_agent():
    return Agent(
        name="StudyScout",
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[ExaTools(), YouTubeTools()],
        markdown=True,
        description="You are a study partner who assists users in finding resources, answering questions, and providing explanations on various topics.",
        instructions=[
            "Use Exa to search for relevant information on the given topic and verify information from multiple reliable sources.",
            "Break down complex topics into digestible chunks and provide step-by-step explanations with practical examples.",
            "Share curated learning resources including documentation, tutorials, articles, research papers, and community discussions.",
            "Recommend high-quality YouTube videos and online courses that match the user's learning style and proficiency level.",
            "Suggest hands-on projects and exercises to reinforce learning, ranging from beginner to advanced difficulty.",
            "Create personalized study plans with clear milestones, deadlines, and progress tracking.",
            "Provide tips for effective learning techniques, time management, and maintaining motivation.",
            "Recommend relevant communities, forums, and study groups for peer learning and networking.",
        ],
    )

agent = get_agent()

# Chat interface
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area("You:", "", height=80)
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.spinner("StudyScout is thinking..."):
        response = agent.run(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": response})

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"<div style='text-align:right; background:#e6f7ff; color:#000; padding:8px; border-radius:8px; margin:4px 0; width:100%;'>👤 <b>You:</b> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        content = msg["content"]
        if hasattr(content, "content"):
            content = content.content
        if not isinstance(content, str):
            content = str(content)
        st.markdown(
            f"""
            <div style='text-align:left; background:#f6f6f6; color:#000; padding:8px; border-radius:8px; margin:4px 0; width:100%;'>
            🤖 <b>StudyScout:</b><br><div style='white-space:pre-wrap'>{content}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.caption("Made with ❤️ using agno, OpenAI, Exa, and Streamlit.")
