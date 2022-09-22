import streamlit as st

from views import Pages



list_of_pages = [
    "About Project MabuhAI",
    "Demographics of the Philippines",
    "Factors why Filipinos are Unbanked",
    "The Team",
    "Test Page"
]

st.sidebar.title(':scroll: Project MabuhAI')
st.sidebar.markdown('by Group Monty-Python | DSFC10')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "About Project MabuhAI":
    Pages.introduction()

elif selection == "Demographics of the Philippines":
    Pages.demog()

elif selection == "Factors why Filipinos are Unbanked":
    Pages.show_factors()

elif selection == "The Team":
    Pages.the_team()

elif selection == "Test Page":
    tab1, tab2 = st.tabs(["📈 Test Chart", "🗃 Test Data"])

    tab1.subheader('Is this better?')
    tab1.image("image2.jpg")
    tab2.subheader('Should we use Tabs instead?')
    tab2.image("image2.jpg")