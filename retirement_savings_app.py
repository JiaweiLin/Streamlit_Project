#__import__('pysqlite3')
#import sys
#sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from openai import OpenAI
from helper_functions import llm

def calculate_retirement_savings(current_age, retirement_age, current_savings, monthly_savings, expected_return):
    years_until_retirement = retirement_age - current_age
    future_value = current_savings * (1 + expected_return) ** years_until_retirement
    
    for i in range(years_until_retirement):
        future_value += monthly_savings * 12 * (1 + expected_return) ** (years_until_retirement - i)
    
    return future_value

def calculate_cpf_savings(current_age, retirement_age, cpf_savings, monthly_income, expected_cpf_rate):
    years_until_retirement = retirement_age - current_age
    current_savings = cpf_savings

    for year in range(1, years_until_retirement + 1):
        # Calculate monthly CPF contributions for the year
        annual_contribution = monthly_income * expected_cpf_rate * 12
        
        # Add annual contribution to savings
        current_savings += annual_contribution
        
        # Calculate and add interest at year end
        interest_earned = current_savings * 0.04
        current_savings += interest_earned

    return current_savings

def get_ai_suggestion(projected_assets, total_needed, shortfall):
    prompt = f"""
    Based on the following retirement savings information, provide a brief suggestion on whether the user has enough savings for retirement in Singapore:
    
    - Projected total assets (Personal savings + CPF savings) for retirement: ${projected_assets:,.2f}
    - Total savings needed for retirement: ${total_needed:,.2f}
    - Shortfall: ${shortfall:,.2f}
    
    Please provide a concise response (4-5 sentences) that includes whether they are on track, and if not, what they should consider doing, for example suggest which CPF Life Plan to use from https://www.cpf.gov.sg/service/article/what-are-the-cpf-life-plans-available-and-which-is-the-right-plan-for-me
    """
    
    messages=[
        {"role": "system", "content": "You are a helpful customer service officer from Central Provident Fund Board Singapore who specializes in providing advice on retirement planning in Singapore."},
         {"role": "user", "content": prompt}
    ]

    response = llm.get_completion_by_messages(messages).strip()
    return response