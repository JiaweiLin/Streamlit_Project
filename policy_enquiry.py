import streamlit as st
from cpf_info_search import search_cpf_info
from helper_functions.utility import check_password

# Check if the password is correct.  
if not check_password():  
    st.stop()

#form = st.form(key="form")

# Streamlit UI
st.title("Enquiry on CPF Policies & Schemes")

user_query = st.text_input("Enter your query about CPF policies & schemes:")
st.caption("_Please add the word 'CPF' in front of the policy/scheme/term if there is no result_")

if user_query:
    with st.spinner("Searching for information..."):
        result = search_cpf_info(user_query)
        st.write(result)

#form.subheader("Prompt")
#user_prompt = form.text_area("Enter your prompt here", height=200)
#if form.form_submit_button("Submit"):
#    st.toast(f"User Input Submitted - {user_prompt}")
#    response = search_cpf_website(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
#    st.write(response)
#    print(f"User Input is {user_prompt}")