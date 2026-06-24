import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR PASSWORD",
    database="business_ai"
)

query = "SELECT * FROM sales"

df = pd.read_sql(query, conn)

conn.close()

print(df.head())

# explore coloums

print(df.columns)
print(df.shape)
print(df.info())

# required calculations

total_sales = df['Sales'].sum()

total_profit = df['Profit'].sum()

total_orders = df['Order ID'].nunique()

df['Order Date'] = pd.to_datetime(df['Order Date'])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)


top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
region_sales = (
    df.groupby('Region')['Sales']
    .sum()
)

# Build the first 'Streamlit page'

import streamlit as st

st.write(df.head())

# headings 

st.title("Business Intelligence Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"₹{total_sales:,.2f}")

with col2:
    st.metric("Total Profit", f"₹{total_profit:,.2f}")

with col3:
    st.metric("Total Orders", total_orders)

# monthly sales trend

st.title('MONTHLY_SALES')
st.line_chart(
    monthly_sales,
    x="Order Date",
    y="Sales"
)

#sales by region

st.title('REGION_SALES')
st.bar_chart(region_sales,color="red") 

# top 10 product 

st.title('TOP_PRODUCTS')
st.bar_chart(top_products, color='grey')


# region

region = st.selectbox(
    "Select Region",
    df["Region"].unique()
)

filtered_df = df[df["Region"] == region]

st.write(filtered_df)
