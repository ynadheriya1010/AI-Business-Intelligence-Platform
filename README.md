# AI Business Intelligence Platform

## Overview

AI Business Intelligence Platform is a Multi-Agent AI system that allows users to ask business questions in natural language and receive data-driven insights, forecasts, document intelligence, and strategic recommendations.

The platform combines SQL generation, forecasting, Retrieval-Augmented Generation (RAG), and decision support within a unified Streamlit dashboard.
The application is built with Python, Streamlit, Groq LLM, MySQL, LangChain, ChromaDB, and Prophet, providing an interactive dashboard for data-driven decision-making.

---

## 🎯 Project Highlights

* Multi-Agent AI Architecture
* Natural Language to SQL Conversion
* Automated Business Analytics
* Sales & Profit Forecasting
* Retrieval-Augmented Generation (RAG)
* AI-Powered Decision Support
* Interactive Plotly Dashboards
* Query History & Report Export
* Groq-powered LLM Inference



## Multi-Agent Architecture

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

## 🛠️ Tech Stack 
Language: Python
Frontend: Streamlit
LLM: Groq API (Llama 3.3 70B Versatile)
Database: MySQL
Vector Database: ChromaDB
Framework: LangChain
Forecasting: Prophet
Visualization: Plotly, Pandas
Embeddings: HuggingFace Sentence Transformers


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
 ## 🔄 Workflow

**User Query** → **Coordinator Agent** → **SQL / Forecast / RAG / Decision Agent** → **Business Insights** → **Interactive Streamlit Dashboard**

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ynadheriya1010/AI-Business-Intelligence-Platform.git

cd AI-Business-Intelligence-Platform
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_groq_api_key

DB_HOST=your_database_host
DB_PORT=3306
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_NAME=business_ai
```

### 4. Create the Vector Database

```bash
python vector_db.py
```

### 5. Run the Application

```bash
streamlit run app.py
```


## Future Enhancements

* Chat-based Interface
* Dynamic Chart Selection
* Cloud Deployment
* Real-Time Business Monitoring
* Multi-Database Support

---

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

## Author

Yash Nadheriya

Electronics and Instrumentation Engineering

Thapar Institute of Engineering & Technology
"# AI-Business-Intelligence-Platform" 



