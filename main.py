import streamlit as st

from views import Pages



list_of_pages = [
    "Page No. 1 Title",
    "Demographics of the Philippines",
    "Factors why Filipinos are Unbanked",
]

st.sidebar.title(':scroll: Group 1 - Monty Python')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Page No. 1 Title":
    Pages.introduction()

elif selection == "Demographics of the Philippines":
    Pages.demog()

elif selection == "Factors why Filipinos are Unbanked":
    Pages.show_factors()
