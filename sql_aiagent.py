from dotenv import load_dotenv
import pandas as pd
import os
import google.generativeai as genai
import mysql.connector

# ==========================
# Load API Key
# ==========================

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================
# Database Connection
# ==========================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your password",
    database="business_ai"
)

# ==========================
# Get Business Data
# ==========================

query = """
SELECT
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

df = pd.read_sql(query, conn)

print("\nDATA")
print(df)

# ==========================
# Convert Data To Text
# ==========================

data_text = df.to_string(index=False)

# ==========================
# AI Report Agent
# ==========================

report_prompt = f"""
You are a Senior Business Intelligence Manager.

Analyze the business data below:

{data_text}

Generate a professional report with:

1. Executive Summary
2. Key Findings
3. Business Risks
4. Recommendations
5. Conclusion

Requirements:
- Professional business language
- Mention best and worst performing regions
- Mention profit trends
- Give strategic recommendations
- Maximum 300 words
"""

try:

    report = model.generate_content(
        report_prompt
    )

    print("\n")
    print("=" * 60)
    print("AI BUSINESS REPORT")
    print("=" * 60)

    print("\n")
    print(report.text)

except Exception as e:

    print("\nREPORT AGENT ERROR:")
    print(e)

conn.close()

import streamlit as st

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    layout="wide"
)

# ==========================
# Agent Functions
# ==========================

def sql_agent(question):
    return f"""
    🔍 SQL Agent Activated

    Question:
    {question}
    
    Running SQL query against the database...
    """

def report_agent():
    return """
    📊 Report Agent Activated

    Generating Business Report...
    """

def forecast_agent():
    return """
    📈 Forecast Agent Activated

    Predicting Future Sales...
    """

# ==========================
# UI
# ==========================

st.title("AI Business Intelligence Platform")

question = st.text_input(
    "Ask a business question",
    placeholder="e.g., What are the sales by region? or Forecast next quarter"
)

# ==========================
# Coordinator Agent
# ==========================

if st.button("Submit", key="main_submit"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
        q = question.lower()
        results = []

        # SQL Agent - triggers for data queries
        if any(keyword in q for keyword in ["sales", "profit", "region", "category", "product", "customer", "revenue", "data"]):
            results.append(sql_agent(question))

        # Forecast Agent - triggers for predictions
        if any(keyword in q for keyword in ["forecast", "predict", "future", "next month", "next 3 months", "next quarter", "projection", "trend"]):
            results.append(forecast_agent())

        # Report Agent - triggers for summaries
        if any(keyword in q for keyword in ["report", "summary", "analysis", "overview", "breakdown"]):
            results.append(report_agent())

        # No Match
        if len(results) == 0:
            st.warning("⚠️ No suitable agent found. Try asking about: sales, forecasts, or reports")
        else:
            # Display Results
            st.markdown("---")
            for result in results:
                st.success(result)
            st.markdown("---")