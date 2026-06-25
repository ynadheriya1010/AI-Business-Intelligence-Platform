# AI Business Intelligence Platform

## Overview

AI Business Intelligence Platform is a Multi-Agent AI system that allows users to ask business questions in natural language and receive data-driven insights, forecasts, document intelligence, and strategic recommendations.

The platform combines SQL generation, forecasting, Retrieval-Augmented Generation (RAG), and decision support within a unified Streamlit dashboard.

---

## Features

### SQL Agent

* Converts natural language questions into SQL queries.
* Retrieves data from MySQL databases.
* Displays query results and business analytics.

### Analytics Agent

* Generates business insights from query results.
* Provides recommendations and impact analysis.

### Forecast Agent

* Uses Facebook Prophet for time-series forecasting.
* Predicts future Sales, Profit, and Quantity trends.
* Generates interactive forecast visualizations.

### RAG Agent

* Answers questions from PDF documents.
* Uses ChromaDB and HuggingFace embeddings.
* Provides document intelligence and report summaries.

### Decision Agent

* Combines SQL insights, forecasts, and document knowledge.
* Generates business recommendations and strategic decisions.

### Coordinator Agent

* Automatically routes user questions to the appropriate AI agent.

---

## Architecture

User Question

↓

Coordinator Agent

↓

├── SQL Agent

├── Forecast Agent

├── RAG Agent

└── Decision Agent

↓

Streamlit Dashboard

---

## Tech Stack

* Python
* Streamlit
* Ollama
* Qwen 2.5
* MySQL
* Pandas
* Plotly
* Prophet
* ChromaDB
* LangChain
* HuggingFace Embeddings

---

## Example Questions

### SQL Agent

* What are the top 5 products by revenue?
* Which region generated the highest profit?
* Show sales by category.

### Forecast Agent

* Forecast sales for the next quarter.
* Predict profit for the next 6 months.
* Forecast quantity demand next year.

### RAG Agent

* Summarize the annual report.
* What does the company policy say about discounts?
* Explain the revenue trends in the report.

### Decision Agent

* Should we increase inventory next quarter?
* Which region deserves more marketing budget?
* Should we focus on Technology products?

---

## Installation

### Clone Repository

git clone https://github.com/yourusername/AI-Business-Intelligence-Platform.git

cd AI-Business-Intelligence-Platform

### Install Dependencies

pip install -r requirements.txt

### Install Ollama Model

ollama pull qwen2.5:7b

### Create Vector Database

python vector_db.py

### Run Application

streamlit run app.py

---

## Future Enhancements

* Chat-based Interface
* Dynamic Chart Selection
* Cloud Deployment
* Real-Time Business Monitoring
* Multi-Database Support

---

## Author

Yash Nadheriya

Electronics and Instrumentation Engineering

Thapar Institute of Engineering & Technology
"# AI-Business-Intelligence-Platform" 

## Screenshots

### SQL Agent

![SQL Dashboard](screenshots/sql_dashboard.png)
![SQL Dashboard](screenshots/sql_dashboard2.png)

### Forecast Agent

![Forecast Dashboard](screenshots/forecast_dashboard.png)
![Forecast Dashboard](screenshots/forecast_dashboard2.png)


### RAG Agent

![RAG Dashboard](screenshots/rag_dashboard.png)



### Decision Agent

![Decision Dashboard](screenshots/decision_dashboard.png)
![Decision Dashboard](screenshots/decision_dashboard2.png)


