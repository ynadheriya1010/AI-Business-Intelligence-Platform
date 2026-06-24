def route_question(question):

    q = question.lower()

    decision_keywords = [
        "should",
        "recommend",
        "recommendation",
        "strategy",
        "increase",
        "decrease",
        "focus",
        "invest",
        "budget",
        "inventory",
        "expand"
    ]

    forecast_keywords = [
        "forecast",
        "predict",
        "future",
        "next month",
        "next quarter",
        "next year",
        "next 3 months",
        "next 6 months",
        "sales forecast",
        "profit forecast",
        "quantity forecast"
    ]

    rag_keywords = [
        "document",
        "documents",
        "report",
        "annual report",
        "policy",
        "policies",
        "handbook",
        "manual",
        "pdf",
        "summarize",
        "summary"
    ]

    # Decision First
    for keyword in decision_keywords:
        if keyword in q:
            return "decision"

    # Forecast Second
    for keyword in forecast_keywords:
        if keyword in q:
            return "forecast"

    # RAG Third
    for keyword in rag_keywords:
        if keyword in q:
            return "rag"

    return "sql"