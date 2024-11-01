import streamlit as st
import random
import yaml

# Load tech questions from the YAML file
def load_questions(yaml_file):
    with open(yaml_file, 'r') as file:
        questions_config = yaml.safe_load(file)
    return questions_config['tech_questions']

# Load questions
tech_questions = load_questions("questions.yaml")

# Initialize session state for question
if 'random_question' not in st.session_state:
    st.session_state.random_question = random.choice(tech_questions)  # Set a default question

# Display random question with enhanced styling and hyperlink in title
st.markdown(
    """
    <h1 style="text-align:center;">
        <a href="https://linktr.ee/tikidata_analytics" target="_blank" style="text-decoration:none; color:#213555;">
            Random Tech Question by Tikidata Analytics
        </a>
    </h1>
    """,
    unsafe_allow_html=True
)

# Highlighted question display
st.markdown(
    f"""
    <div style="background-color:#D8C4B6;padding:20px;border-radius:5px;margin:10px 0;">
        <h2 style="color:#213555;text-align:center;">{st.session_state.random_question}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Button to get a new question
if st.button("Get Another Question"):
    st.session_state.random_question = random.choice(tech_questions)  # Change question on button click

