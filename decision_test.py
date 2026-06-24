from decision_agent import generate_decision

decision = generate_decision(
    question="Should we increase inventory next quarter?",
    sql_result="Sales increased 15%",
    forecast_result="Forecast predicts 18% growth",
    rag_result="Company policy allows inventory increase up to 20%"
)

print(decision)