from ollama import chat

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

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]