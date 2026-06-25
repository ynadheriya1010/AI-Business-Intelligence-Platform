import pandas as pd
import mysql.connector
from prophet import Prophet
from dotenv import load_dotenv
import os



def forecast_agent(question):

    # ==========================
    # Metric Selection
    # ==========================

    q = question.lower()

    if "profit" in q:
        metric = "Profit"

    elif "quantity" in q:
        metric = "Quantity"

    else:
        metric = "Sales"

    # ==========================
    # Forecast Period
    # ==========================

    if "next month" in q:
        periods = 30

    elif "quarter" in q:
        periods = 90

    elif "6 month" in q:
        periods = 180

    elif "year" in q:
        periods = 365

    else:
        periods = 90

    # ==========================
    # Database Connection
    # ==========================

    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YN@789",
    database="business_ai"
)

    query = f"""
    SELECT
        `Order Date`,
        {metric}
    FROM sales
    """

    df = pd.read_sql(query, conn)

    conn.close()

    # ==========================
    # Data Preparation
    # ==========================

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    daily_data = (
        df.groupby("Order Date")[metric]
        .sum()
        .reset_index()
    )

    daily_data.columns = [
        "ds",
        "y"
    ]

    # ==========================
    # Prophet Model
    # ==========================

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(daily_data)

    # ==========================
    # Forecast
    # ==========================

    future = model.make_future_dataframe(
        periods=periods
    )

    forecast = model.predict(future)

    future_data = forecast.tail(periods)

    # ==========================
    # Summary
    # ==========================

    avg_value = future_data["yhat"].mean()

    max_value = future_data["yhat"].max()

    min_value = future_data["yhat"].min()

    summary = {
        f"Average {metric}":
            round(avg_value, 2),

        f"Maximum {metric}":
            round(max_value, 2),

        f"Minimum {metric}":
            round(min_value, 2)
    }

    return summary, forecast, metric