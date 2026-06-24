from ollama import chat
import mysql.connector
import pandas as pd


def generate_sql(question):

    prompt = f"""
You are an expert MySQL developer.

Database: business_ai

Table: sales

IMPORTANT:
Columns containing spaces MUST use backticks (`).

Examples:
`Product Name`
`Order Date`
`Customer Name`
`Ship Mode`
`Sub-Category`
`Row ID`

Columns:

`Row ID`
`Order ID`
`Order Date`
`Ship Date`
`Ship Mode`
`Customer ID`
`Customer Name`
`Segment`
`Country`
`City`
`State`
`Postal Code`
`Region`
`Product ID`
`Category`
`Sub-Category`
`Product Name`
`Sales`
`Quantity`
`Discount`
`Profit`

User Question:
{question}

Rules:
1. Return ONLY valid MySQL query
2. Do NOT explain
3. Do NOT use markdown
4. Do NOT use ```sql
5. Always use backticks around column names that contain spaces
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

    sql = response["message"]["content"]

    # Clean LLM response
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql


def run_sql(question):

    sql_query = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql_query)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR PASSWORD",
        database="business_ai"
    )

    try:
        df = pd.read_sql(sql_query, conn)
        conn.close()

        return sql_query, df

    except Exception as e:
        conn.close()

        print("\nSQL Execution Error:")
        print(e)

        raise e