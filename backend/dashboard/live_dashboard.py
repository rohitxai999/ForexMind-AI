"""
ForexMind AI
Day 8

Live Dashboard
"""

import streamlit as st

from portfolio.portfolio_manager import portfolio_manager
from agents.economic_news_agent import economic_news_agent

st.set_page_config(
    page_title="ForexMind AI",
    layout="wide",
)

st.title("📈 ForexMind AI Dashboard")

st.markdown("---")

summary = portfolio_manager.portfolio_summary()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Balance", f"${summary['balance']}")

with col2:
    st.metric("Open Trades", summary["open_trades"])

with col3:
    st.metric("Win Rate", f"{summary['win_rate']}%")

st.markdown("---")

st.subheader("📰 Economic News")

news = economic_news_agent.check_trading_status()

if news["trade_allowed"]:
    st.success(news["reason"])
else:
    st.error(news["reason"])

st.markdown("---")

st.subheader("📊 Portfolio Summary")

st.json(summary)