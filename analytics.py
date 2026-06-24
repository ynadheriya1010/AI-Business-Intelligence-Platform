import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your password ",
    database="business_ai"
)

# sales_query = """
# SELECT SUM(sales) AS Total_sales
# FROM sales; 
# """
# profit_querry= """
# SELECT SUM(profit) AS Total_profit
# FROM sales;
# """
# region_querry= """
# SELECT Region,
# SUM(Sales) AS Region_Sales
# FROM sales
# GROUP BY Region;
# """

# sales_df = pd.read_sql(sales_query, conn)
# profit_df = pd.read_sql(profit_querry, conn)
# region_df = pd.read_sql(region_querry, conn)

# print(sales_df)
# print(profit_df)
# print(region_df)

# conn.close()


# method 2

queries = {
    "total_sales": """
        SELECT SUM(Sales) AS Total_Sales
        FROM sales;
    """,

    "total_profit": """
        SELECT SUM(Profit) AS Total_Profit
        FROM sales;
    """,

    "sales_by_region": """
        SELECT Region,
        SUM(Sales) AS Region_Sales
        FROM sales
        GROUP BY Region;
    """
}
df = pd.read_sql(queries["sales_by_region"], conn)

print(df)
conn.close()