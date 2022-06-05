import streamlit as st
import streamlit.report_thread
import streamlit_analytics


with streamlit_analytics.track():
    st.text_input("Write your name")
    st.selectbox("Select your favorite", ["guvi", "data", "science"])
    st.button("Click me")
    if streamlit_analytics.split_test("option a", 2):
        st.button("Is this button text better?")

    if streamlit_analytics.split_test("option b", 2):
        st.button("...or this one?")
