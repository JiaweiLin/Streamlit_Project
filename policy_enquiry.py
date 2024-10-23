import streamlit as st
from cpf_info_search import search_cpf_info
from helper_functions.utility import check_password

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Streamlit UI
st.title("📝 Enquiry on CPF Policies & Schemes")

user_query = st.text_input("Enter your query about CPF policies & schemes:")
st.caption("_Please add the word 'CPF' in front of the policy/scheme/term if there is no result_")

if user_query:
    with st.spinner("Searching for information..."):
        result = search_cpf_info(user_query)
        st.write(result)