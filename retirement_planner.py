__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from retirement_savings_app import calculate_retirement_savings, get_ai_suggestion
from helper_functions.utility import check_password

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.title("💰 Retirement Savings Calculator")
st.write("Use this calculator to estimate if you're on track for a comfortable retirement.")

col1, col2 = st.columns(2)

with col1:
    current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30)
    current_savings = st.number_input("Current Savings ($)", min_value=0, value=10000)
    expected_return = st.slider("Expected Annual Return (%)", min_value=1, max_value=15, value=7, step=1)

with col2:
    retirement_age = st.number_input("Retirement Age", min_value=current_age + 1, max_value=100, value=65)
    monthly_contribution = st.number_input("Monthly CPF Contribution ($)", min_value=0, value=500)
    life_expectancy = st.number_input("Life Expectancy", min_value=retirement_age + 1, max_value=120, value=85)

expected_expenses = st.number_input("Expected Annual Expenses in Retirement ($)", min_value=0, value=40000)

if st.button("Calculate"):
    if retirement_age <= current_age:
        st.error("Retirement age must be greater than current age.")
    elif life_expectancy <= retirement_age:
        st.error("Life expectancy must be greater than retirement age.")
    else:
        projected_savings = calculate_retirement_savings(current_age, retirement_age, current_savings, monthly_contribution, expected_return / 100)
        years_in_retirement = life_expectancy - retirement_age
        total_needed = expected_expenses * years_in_retirement
        
        st.subheader("Results")
        st.write(f"Projected Savings at Retirement: ${projected_savings:,.2f}")
        st.write(f"Total Needed for Retirement: ${total_needed:,.2f}")
        
        if projected_savings >= total_needed:
            shortfall = 0
            additional_monthly = 0
        else:
            shortfall = total_needed - projected_savings
            additional_monthly = shortfall / ((1 + expected_return / 100) ** (retirement_age - current_age) - 1) / (expected_return / 1200)
        
        ai_suggestion = get_ai_suggestion(projected_savings, total_needed, shortfall, additional_monthly)
        st.subheader("AI Suggestion")
        st.write(ai_suggestion)