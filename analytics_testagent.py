import pandas as pd
from analytics_agent import generate_insights

question = "highest sales region"

df = pd.DataFrame({
    "Region": ["West"],
    "TotalSales": [713471]
})

insights = generate_insights(
    question,
    df
)

print(insights)