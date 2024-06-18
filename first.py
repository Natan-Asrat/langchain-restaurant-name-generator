import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")

cuisine = st.sidebar.checkbox("Pick a cuisine", (
    "Italian",
    "Ethiopian",
    "Mexican",
    "American"
))

