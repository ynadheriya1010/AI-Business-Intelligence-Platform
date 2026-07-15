from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_insights(question, df):

    data_text = df.to_string(index=False)

    prompt = f"""
You are a Senior Business Analyst.

User Question:
{question}

Query Result:
{data_text}

Generate:

1. Key Insights
2. Business Impact
3. Recommendations

Keep response under 5 bullet points.
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
    print(type(response))
    print(response)

    answer = response.choices[0].message.content
    return answer
    