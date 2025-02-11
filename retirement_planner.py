import streamlit as st
from retirement_savings_app import calculate_retirement_savings, get_ai_suggestion, calculate_cpf_savings
from helper_functions.utility import check_password

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.title("💰 Retirement Savings Calculator")
st.write("Use this calculator to estimate if you are on track for a comfortable retirement in Singapore.")

col1, col2 = st.columns(2)

with col1:
    current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30)
    current_savings = st.number_input("Current Savings ($)", min_value=0, value=10000)
    expected_expenses = st.number_input("Expected Annual Expenses After Retirement ($)", min_value=0, value=40000)
    cpf_savings = st.number_input("Current CPF Savings ($) - Assume 4% interest annually", min_value=0, value=10000)
    monthly_income = st.number_input("Monthly Income Before Retirement ($)", min_value=0, value=4000)
    
with col2:
    retirement_age = st.number_input("Retirement Age", min_value=65, max_value=100, value=65)
    monthly_savings = st.number_input("Monthly Savings After Expenses ($)", min_value=0, value=500)
    life_expectancy = st.number_input("Life Expectancy", min_value=retirement_age, max_value=120, value=85)
    monthly_payout = st.number_input("Monthly CPF Payout After 65 ($)", min_value=0, value=500)
    expected_cpf_rate = st.slider("Expected CPF contribution rate (%)", min_value=0.10, max_value=37.00, value=37.00, step=0.50)

expected_return = st.slider("Expected Annual Return on Savings (%)", min_value=0.10, max_value=10.00, value=3.00, step=0.10)


if st.button("Calculate"):
    if retirement_age <= current_age:
        st.error("Retirement age must be greater than current age.")
    elif life_expectancy <= retirement_age:
        st.error("Life expectancy must be greater than retirement age.")
    else:
        projected_savings = calculate_retirement_savings(current_age, retirement_age, current_savings, monthly_savings, expected_return / 100.00)
        projected_cpf_savings = calculate_cpf_savings(current_age, retirement_age, cpf_savings, monthly_income, expected_cpf_rate / 100.00)
        
        years_in_retirement = life_expectancy - retirement_age
        total_needed = expected_expenses * years_in_retirement
        total_payout = monthly_payout * 12 * (life_expectancy - 65)
        
        st.subheader("Results")
        st.write(f"Projected Savings at Retirement: ${projected_savings:,.2f}")
        st.write(f"Projected CPF Savings at Retirement: ${projected_cpf_savings:,.2f}")
        st.write(f"Projected Total CPF Payout till death (not included in suggestion analysis below as it is assumed to be part of CPF savings): ${total_payout:,.2f}")
        st.write(f"Total Needed for Retirement: ${total_needed:,.2f}")
        
        if projected_savings + projected_cpf_savings >= total_needed:
            shortfall = 0
        else:
            shortfall = total_needed - projected_savings - projected_cpf_savings
        
        ai_suggestion = get_ai_suggestion(projected_savings + projected_cpf_savings, total_needed, shortfall)
        ai_suggestion_stripped = ai_suggestion.replace("$", " ")
        st.subheader("Suggestion")
        st.write(ai_suggestion_stripped)