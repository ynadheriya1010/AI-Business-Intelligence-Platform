from ollama import chat


def generate_decision(
    question,
    sql_result="",
    forecast_result="",
    rag_result=""
):

    prompt = f"""
You are a Senior Business Consultant.

Business Question:
{question}

SQL Analysis:
{sql_result}

Forecast Analysis:
{forecast_result}

Document Analysis:
{rag_result}

Provide:

1. Recommendation
2. Supporting Reasons
3. Potential Risks
4. Next Action

Keep the answer concise.
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