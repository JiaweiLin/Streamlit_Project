__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from openai import OpenAI
from helper_functions import llm

def calculate_retirement_savings(current_age, retirement_age, current_savings, monthly_contribution, expected_return):
    years_until_retirement = retirement_age - current_age
    future_value = current_savings * (1 + expected_return) ** years_until_retirement
    
    for i in range(years_until_retirement):
        future_value += monthly_contribution * 12 * (1 + expected_return) ** (years_until_retirement - i)
    
    return future_value

def get_ai_suggestion(projected_savings, total_needed, shortfall, additional_monthly):
    prompt = f"""
    Based on the following retirement savings information, provide a brief suggestion on whether the user has enough savings for retirement:
    
    - Projected Savings at Retirement: ${projected_savings:,.2f}
    - Total Needed for Retirement: ${total_needed:,.2f}
    - Shortfall: ${shortfall:,.2f}
    - Suggested Additional Monthly Contribution: ${additional_monthly:,.2f}
    
    Please provide a concise response (2-3 sentences) that includes whether they're on track, and if not, what they should consider doing.
    """
    
    messages=[
        {"role": "system", "content": "You are a helpful customer service officer from Central Provident Fund Board Singapore specializing in retirement planning."},
         {"role": "user", "content": prompt}
    ]

    response = llm.get_completion_by_messages(messages).strip()
    return response