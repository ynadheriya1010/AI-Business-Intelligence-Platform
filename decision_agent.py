from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_decision(question, sql_result, forecast_result, rag_result):

    prompt = f"""
You are a Senior Business Decision Consultant.

User Question:
{question}

SQL Analysis:
{sql_result}

Forecast Analysis:
{forecast_result}

RAG Knowledge:
{rag_result}

Provide:

1. Final Business Decision
2. Reason
3. Recommended Action

Keep response concise.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content