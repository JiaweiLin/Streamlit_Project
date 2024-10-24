import streamlit as st

# Title Section
st.title("👨‍💻	About Us")

# Project Scope Section
st.header("Project Scope")
st.markdown("""
**Title**: CPF Policy Enquiry and Retirement Savings Calculator

**Objective**: The CPF Policy Enquiry portal allows users to enter queries related to CPF 
policies and schemes. Users will receive answers which are based on the CPF Policy FAQ pages and CPF
Overview page. The Retirement Savings Calculator provides users with insights into retirement 
planning based on personal savings, CPF savings and expenditure. This calculator will help users make 
informed decisions for their future retirement based on personalized input data.
""")

# Target Audience Section
st.header("Target Audience")
st.markdown("This application is designed for:")
st.markdown("""
* Users who have queries related to CPF policies and schemes
* Individuals planning for retirement in Singapore
""")

# Data Sources Section
st.header("Data Sources")
st.markdown("""
* **CPF Data**: Information from CPF Policy FAQs and CPF Overview page is used to support 
queries based  on CPF policies and schemes. For more details, visit 
[CPF Policy FAQs](https://www.cpf.gov.sg/member/infohub/cpf-clarifies/policy-faqs) and [CPF Overview](https://www.cpf.gov.sg/member/cpf-overview). 
Information from an article on CPF Life is used to support the Retirements Savings Calculator, can visit [CPF Life](https://www.cpf.gov.sg/service/article/what-are-the-cpf-life-plans-available-and-which-is-the-right-plan-for-me).           
""")

# Key Features Section
st.header("Key Features")
st.markdown("""
* **CPF Policy Enquiry**: Users can enter queries related to CPF policies and schemes. A detailed and accurate answer will be returned by the application, helping the user understand more about the CPF policy or scheme.

* **Retirement Savings Calculator**: Users can adjust different parameters to see how different financial choices affect their retirement funds, helping them make informed decisions about their financial future, based on accurate and latest information about CPF policies.
""")

# Developer Section
st.header("Developer")
st.markdown("""
This application was developed by **Jiawei Lin** as part of 
**GovTech's AI Champions Bootcamp 2024 - Pilot Run 2nd Cohort**
""")