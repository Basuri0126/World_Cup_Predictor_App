import streamlit as st


# Set page configuration

st.set_page_config(
    page_title="World Cup Predictor App",
    layout="wide",
    initial_sidebar_state="expanded",  # Change to "expanded" if you want the sidebar open by default
    page_icon='pageicon.png'
)

# Define CSS styles
st.markdown(
    """
    <style>
    .header {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .description {
        font-size: 18px;
        text-align: center;
        margin-top: 20px;
    }
    .options {
        font-size: 24px;
        font-weight: bold;
        margin-top: 30px;
    }
    .emoji {
        font-size: 36px;
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Homepage content
st.markdown('<p class="header">Welcome to the World Cup Predictor App! 🏏</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="description" style="font-size: 25px;">This app allows you to make predictions related to cricket matches in the World Cup. You have two main options:</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="options"><span class="emoji">1️⃣</span>Score Predictor</p>'
    '<p class="description" style="font-size: 20px;">Predict the 1st innings score of a cricket match.</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="options"><span class="emoji">2️⃣</span>Win Probability Predictor</p>'
    '<p class="description" style="font-size: 20px;">Predict the probability of a chasing team winning a cricket match.</p>',
    unsafe_allow_html=True,
)

