import mysql.connector
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


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

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Defensive extraction in case the SDK/object shape is ever non-standard
    try:
        sql = response.choices[0].message.content
    except TypeError:
        # Fallback: .choices came back as a single object instead of a list
        choice = response.choices
        sql = choice.message.content

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
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
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