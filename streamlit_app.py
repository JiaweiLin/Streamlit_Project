import streamlit as st

home_page = st.Page("home.py", title="Home Page", icon=":material/home:")
policy_enquiry_page = st.Page("policy_enquiry.py", title="CPF Policy Enquiry", icon=":material/search:")
about_us_page = st.Page("about_us.py", title="About Us", icon=":material/person:")
methodology_page = st.Page("methodology.py", title="Methodology", icon=":material/lightbulb:")
retirement_planner_page = st.Page("retirement_planner.py", title="Retirement Planner", icon=":material/tactic:")

pg = st.navigation([home_page, policy_enquiry_page, retirement_planner_page, about_us_page, methodology_page])
st.set_page_config(page_title="CPF Enquiry Portal", page_icon=":material/dashboard:")
pg.run()