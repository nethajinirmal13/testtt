import streamlit as st
import streamlit_analytics
import streamlit_authenticator as stauth

names = ['nirmal', 'n']
usernames = ['g', 'guvi']
passwords = ['123', '456']


authenticator = stauth.Authenticate(names, usernames)

with streamlit_analytics.track():
    st.text_input("Write your name")
    st.selectbox("Select your favorite", ["cat", "dog", "flower"])
    st.button("Click me")
