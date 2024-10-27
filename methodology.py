import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import os

def load_image(filename):
    """Load an image from a URL."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, 'images', filename)
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        st.error(f"Error loading image from URL: {str(e)}")
        return None
    
st.title("🧠 Methodology")
st.write("1. CPF Policy Enquiry")
st.image(load_image("flowchart1.png"), caption="Data Flow 1")

with st.expander("Data Flow 1: CPF Policy Enquiry and Retirement Savings Calculator"):
    st.write("1. User enters query which is handled by the :blue-background[policy_enquiry.py] script")
    st.write("2. The script :blue-background[cpf_info_search.py] then creates the Agent researcher which has a WebsiteSearchTool to retrieve information from this url :blue[https://www.cpf.gov.sg/member/infohub/cpf-clarifies/policy-faqs.]"
             + " The Agent support researcher is then created, where this Agent also has a WebsiteSearchTool to retrieve information from this url :blue[https://www.cpf.gov.sg/member/cpf-overview if the researcher is unable to find information.]")
    st.write("3. The task for Agent researcher is created where the researcher will find answer to the query from the given URL and WebSiteSearchTool. The Agent is required to provide a detailed and informative response to the query, maintaining a helpful and friendly tone.")
    st.write("4. The task for Agent support researcher is created where the support researcher will review the response drafted by the researcher for the enquiry and ensure that the answer is comprehensive and accurate, making sure that the reference URL is present in the response."
             + " If the support researcher finds information, then a detailed response should be sent back to fully address the enquiry. The support researcher should also maintain a helpful and friendly tone throughout.")
    st.write("5. To prevent prompt injection and minimize chance of app exploitation, the agents are tasked not to provide an answer if an answer cannot be found and the query is not related to Central Provident Fund. A reply will be sent back mentioning that the CPF Policy FAQs do not have the information.")

st.write("2. Retirement Savings Calculator")
st.image(load_image("calculator_flowchart1.png"), caption="Data Flow 3")
st.image(load_image("calculator_flowchart2.png"), caption="Data Flow 4")

with st.expander("Data Flow 3 & 4: Retirement Savings Calculator"):
    st.write("1. User enters values which are handled by the :blue-background[retirement_planner.py] script")
    st.write("2. The values to be filled in are :blue[current_age], :blue[current_savings], :blue[expected_expenses], :blue[cpf_savings], :blue[monthly_income], :blue[retirement_age], :blue[monthly_savings], :blue[life_expectancy], :blue[monthly_payout], :blue[expected_cpf_rate] and :blue[expected_annual_return_on_savings_%].")
    st.write("3. One validation check includes verifying that the :blue[retirement_age] must be greater than :blue[current_age]. Another validation check includes verifying that :blue[life_expectancy] must be greater than :blue[retirement_age].")
    st.write("4. If there are no validation errors, then the application will proceed to calculate :blue[projected_retirement_savings] and also calculate :blue[projected_CPF_savings]. The calculation logic will be handled by :blue-background[retirement_savings_app.py] script.")
    st.write("5. The :blue[total_retirement_expenses] is then calculated. If the sum of :blue[projected_retirement_savings] and :blue[projected_cpf_savings] is greater than :blue[total_retirement_expenses] needed, then there is no :blue[shortfall]. Else, the :blue[shortfall] value is calculated.")
    st.write("6. These 4 values :blue[projected_retirement_savings], :blue[projected_cpf_savings], :blue[total_retirement_expenses] and :blue[shortfall] are included in the prompt chain to be sent to OpenAI, asking OpenAI to provide a brief suggestion on whether the user has enough savings for retirement in Singapore. OpenAI should also provide a concise response (4-5 sentences) that includes whether they are on track, and if not, what they should consider doing, for example suggest which CPF Life Plan to use.")