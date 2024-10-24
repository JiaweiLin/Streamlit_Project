import streamlit as st

st.title("🏠 Home")
st.write("Welcome to the Home page! This app offers two services - CPF Policy Enquiry and Retirement Savings Calculator.")
st.write("For the CPF Policy Enquiry, users can enter queries related to CPF policies and schemes. A detailed and accurate answer will be returned by the application, helping the user understand more about the CPF policy or scheme.")
st.write("For the Retirement Savings Calculator, users can adjust different parameters to see how different financial choices affect their retirement funds, helping them make informed decisions about their financial future, based on accurate and latest information about CPF policies.")

with st.expander("Disclaimer"):
    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")
    st.write("Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")
    st.write("Always consult with qualified professionals for accurate and personalized advice.")