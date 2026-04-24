import streamlit as st

from ui.styles import load_styles
from ui.pages import home, puzzle_solver, algorithm_check, documentation

st.set_page_config(
    page_title="AI Puzzle Solver",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_styles()

if "page" not in st.session_state:
    st.session_state.page="Home"

if st.session_state.page=="Home":
    home()
elif st.session_state.page=="Puzzle Solver":
    puzzle_solver()
elif st.session_state.page=="Algorithm Check":
    algorithm_check()
else:
    documentation()
