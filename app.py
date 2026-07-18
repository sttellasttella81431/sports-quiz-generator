import streamlit as st
from src.database import setup_and_populate_db
from src.generator import compile_quiz_data

# Initialize the database once
@st.cache_resource
def prepare_database():
    setup_and_populate_db()

prepare_database()

# Page settings
st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏆",
    layout="centered"
)

st.title("🏆 AI-Powered Sports Quiz Generator")
st.write("Generate sports quizzes using RAG (ChromaDB + Live Web Search).")

# Sidebar
st.sidebar.header("Quiz Settings")

sport = st.sidebar.selectbox(
    "Select Sport",
    ["Cricket", "Football", "Badminton", "Tennis", "Basketball"]
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

if "quiz" not in st.session_state:
    st.session_state.quiz = ""
    st.session_state.context = ""

if st.sidebar.button("Generate Quiz"):

    with st.spinner("Generating quiz..."):

        quiz, context = compile_quiz_data(
            sport,
            difficulty
        )

        st.session_state.quiz = quiz
        st.session_state.context = context

if st.session_state.quiz:

    st.subheader("Generated Quiz")

    st.text_area(
        "Quiz",
        st.session_state.quiz,
        height=400
    )

    with st.expander("RAG Context Used"):
        st.write(st.session_state.context)