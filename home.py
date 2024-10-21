import streamlit as st
from helper_functions.utility import check_password

st.title("Home")
st.write("Welcome to the Home page! This app offers two services - CPF Policy Enquiry and Retirement Planning Simulator.")
st.write("For the CPF Policy Enquiry, users can enter queries related to CPF policies and schemes, the app should return an answer.")
st.write("For the retirement planning simulator, users can tweak various parameters to see if their retirement plan is sustainable.")

with st.expander("Disclaimer"):
    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")
    st.write("Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")
    st.write("Always consult with qualified professionals for accurate and personalized advice.")