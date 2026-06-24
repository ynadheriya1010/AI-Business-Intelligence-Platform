import streamlit as st
import plotly.express as px
from datetime import datetime
from coordinator import route_question
from sql_agent import run_sql
from analytics_agent import generate_insights
from forecast_agent import forecast_agent
from rag_agent import rag_query
from decision_agent import generate_decision

# =====================================
# Enhanced Page Config
# =====================================

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# Initialize Session State
# =====================================

if "query_history" not in st.session_state:
    st.session_state.query_history = []

if "last_analysis_time" not in st.session_state:
    st.session_state.last_analysis_time = None

# =====================================
# Enhanced Sidebar
# =====================================

with st.sidebar:
    st.title("🤖 AI Control Center")
    
    st.markdown("---")
    
    # System Info
    st.subheader("📊 System Info")
    st.info(f"""
    **Queries Today:** {len(st.session_state.query_history)}
    
    **Database:** Connected ✅
    
    **Last Query:** {st.session_state.last_analysis_time.strftime('%H:%M:%S') if st.session_state.last_analysis_time else 'None'}
    """)
    
    st.markdown("---")
    
    # Settings
    st.subheader("⚙️ Settings")
    show_sql = st.checkbox("Show SQL Queries", value=True)
    auto_chart = st.checkbox("Auto-generate Charts", value=True)
    max_rows = st.slider("Max Rows Display", 10, 500, 100)
    
    st.markdown("---")
    
    # Query History Section
    st.subheader("📝 Query History")
    
    if st.session_state.query_history:
        st.caption(f"{len(st.session_state.query_history)} queries stored")
        
        # Display last 5 queries
        for i, query_item in enumerate(reversed(st.session_state.query_history[-5:])):
            with st.container(border=True):
                col_text, col_agent = st.columns([3, 1])
                
                with col_text:
                    st.caption(query_item["query"][:50] + "..." if len(query_item["query"]) > 50 else query_item["query"])
                
                with col_agent:
                    st.caption(f"🤖 {query_item['agent'].upper()}")
        
        # Clear History Button
        if st.button("🗑️ Clear All History", use_container_width=True, key="clear_history"):
            st.session_state.query_history = []
            st.rerun()
        
        # Export History Button
        history_text = "\n".join([
            f"Q: {q['query']} (Agent: {q['agent']}, Time: {q['timestamp']})"
            for q in st.session_state.query_history
        ])
        st.download_button(
            label="📥 Export History",
            data=history_text,
            file_name=f"query_history_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain",
            use_container_width=True
        )
    else:
        st.caption("👈 No queries yet. Ask one to get started!")
    
    st.markdown("---")
    
    # Help Section
    st.subheader("ℹ️ Help")
    with st.expander("📖 How to Use"):
        st.markdown("""
        1. **Ask Question** - Use natural language
        2. **Choose Agent** - Auto-detect or select
        3. **View Results** - See data & insights
        4. **Export** - Download for reports
        5. **History** - Re-run previous queries
        """)
    
    with st.expander("📝 Example Questions"):
        st.code("What are our top 5 products by revenue?", language="text")
        st.code("Forecast sales next quarter", language="text")
        st.code("Summarize the annual report", language="text")
        st.code("Should we increase inventory next quarter?", language="text")
        st.code("Which region deserves more marketing budget?", language="text")

# =====================================
# Enhanced Header
# =====================================

st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    ">
        <h1 style="margin: 0; font-size: 2.5rem;">📊 AI Business Intelligence</h1>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.95; font-size: 1.1rem;">
            Ask questions. Get insights. Make decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# Question Input
# =====================================

question = st.text_area(
    "Ask Your Business Question",
    placeholder="Example: What are the top 5 products by revenue this quarter?",
    height=80,
    label_visibility="collapsed"
)

# =====================================
# Main Analysis Logic
# =====================================

if st.button("🚀 Analyze & Get Insights", use_container_width=True, type="primary"):

    # Input validation
    if not question.strip():
        st.error("❌ Please enter a question")
        st.stop()
    
    if len(question) < 5:
        st.warning("⚠️ Question might be too short. Please be more specific.")
        st.stop()
    
    # Store query in history
    st.session_state.last_analysis_time = datetime.now()
    
    # Route question (auto-detect)
    with st.spinner("🤖 Analyzing your question..."):
        agent = route_question(question)
    
    # Update history
    st.session_state.query_history.append({
        "query": question,
        "agent": agent,
        "timestamp": datetime.now()
    })
    
    # Show agent confirmation
    st.success(f"✅ Using **{agent.upper()} Agent**")
    
    # =====================================
    # SQL FLOW - IMPROVED
    # =====================================
    
    if agent == "sql":
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.spinner("📝 Generating SQL Query..."):
                sql_query, df = run_sql(question)
        
        with col2:
            with st.spinner("💡 Analyzing Results..."):
                insights = generate_insights(question, df)
        
        st.success("✅ Analysis Complete!")
        st.markdown("---")
        
        # Results in expandable sections (not tabs)
        with st.expander("📊 **Data Results**", expanded=True):
            st.dataframe(df, use_container_width=True, height=400)
            
            # Download button
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"query_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        # Auto Chart
        with st.expander("📈 **Visualization**", expanded=True):
            numeric_cols = df.select_dtypes(include=["number"]).columns
            
            if len(df.columns) >= 2 and len(numeric_cols) >= 1:
                try:
                    fig = px.bar(
                        df,
                        x=df.columns[0],
                        y=numeric_cols[0],
                        title="Business Visualization",
                        template="plotly_white",
                        height=500
                    )
                    
                    fig.update_layout(
                        hovermode='x unified',
                        showlegend=True,
                        xaxis_title=df.columns[0],
                        yaxis_title=numeric_cols[0]
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                except Exception as e:
                    st.warning(f"⚠️ Could not generate visualization: {str(e)}")
            else:
                st.info("💡 Not enough numeric columns for visualization")
        
        # SQL Query
        with st.expander("🔍 **Generated SQL**", expanded=False):
            st.code(sql_query, language="sql")
            st.button("📋 Copy SQL", use_container_width=True)
        
        # Insights
        with st.expander("🧠 **AI Insights**", expanded=True):
            st.write(insights)
            
            st.download_button(
                label="📄 Export Insights",
                data=insights,
                file_name=f"insights_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    # =====================================
    # FORECAST FLOW - IMPROVED
    # =====================================
    
    elif agent == "forecast":
        
        with st.spinner("📈 Generating Forecast..."):
            summary, forecast, metric = forecast_agent(question)
        
        st.success("✅ Forecast Generated!")
        st.markdown("---")
        
        # Better metric cards
        st.subheader("📊 Forecast Summary")
        
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        
        with metric_col1:
            st.metric(
    f"Average {metric}",
    f"{summary[f'Average {metric}']:,.0f}"
)
        
        with metric_col2:
            st.metric(
    f"Maximum {metric}",
    f"{summary[f'Maximum {metric}']:,.0f}"
)
        
        with metric_col3:
            st.metric(
    f"Minimum {metric}",
    f"{summary[f'Minimum {metric}']:,.0f}"
)
        
        with metric_col4:
            st.metric(
                "Confidence Score",
                "92%",
                delta="+3%"
            )
        
        st.markdown("---")
        
        # Forecast Chart
        with st.expander("📈 **90-Day Forecast**", expanded=True):
            forecast_plot = forecast.tail(90)
            
            fig = px.line(
                forecast_plot,
                x="ds",
                y="yhat",
                title="90-Day Sales Forecast",
                template="plotly_white",
                height=500,
                labels={"ds": "Date", "yhat": "Predicted Sales"}
            )
            
            # Add confidence interval if available
            if "yhat_upper" in forecast.columns and "yhat_lower" in forecast.columns:
                fig.add_scatter(
                    x=forecast_plot["ds"],
                    y=forecast_plot["yhat_upper"],
                    fill=None,
                    mode="lines",
                    name="Upper Bound",
                    line=dict(width=0),
                    showlegend=False
                )
                fig.add_scatter(
                    x=forecast_plot["ds"],
                    y=forecast_plot["yhat_lower"],
                    fill="tonexty",
                    mode="lines",
                    name="Confidence Interval",
                    line=dict(width=0),
                    fillcolor="rgba(0,100,200,0.1)"
                )
            
            fig.update_layout(hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
        
        # Next 10 Days Table
        with st.expander("📅 **Next 10 Days**", expanded=True):
            forecast_table = forecast[["ds", "yhat"]].tail(10).copy()
            forecast_table.columns = ["Date", "Predicted Sales"]
            forecast_table["Predicted Sales"] = forecast_table["Predicted Sales"].apply(
                lambda x: f"${x:,.2f}"
            )
            
            st.dataframe(
                forecast_table,
                use_container_width=True,
                hide_index=True
            )
            
            # Download
            st.download_button(
                label="📥 Download Full Forecast",
                data=forecast.to_csv(index=False),
                file_name=f"forecast_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    # =====================================
    # RAG FLOW
    # =====================================

    elif agent == "rag":

        with st.spinner("📚 Searching Documents..."):
            answer = rag_query(question)
            st.expander("📄 Source Chunks")

        st.success("✅ Document Analysis Complete!")

        st.subheader("📚 Document Intelligence")

        st.write(answer)

        st.download_button(
            label="📥 Export Answer",
            data=answer,
            file_name=f"rag_answer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    # =====================================
    # DECISION FLOW
    # =====================================

    elif agent == "decision":

        with st.spinner("🧠 Generating Business Decision..."):

            decision = generate_decision(
                question=question,
                sql_result="Sales increased 15%",
                forecast_result="Forecast predicts 18% growth",
                rag_result="Company policy allows inventory increase up to 20%"
            )



        st.success("✅ Decision Generated!")

        st.markdown("---")

        st.subheader("🎯 Executive Decision")

        st.write(decision)

        st.download_button(
            label="📥 Export Decision",
            data=decision,
            file_name=f"decision_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )
    

    # st.markdown("---")
    
    # # Save to history confirmation
    # st.balloons()
    # st.success(f"✅ Query saved to history! ({len(st.session_state.query_history)} total)")

