from ai_engine.explainability.market_summary import MarketSummary

market = {
    "trend": "Bullish",
    "momentum": "Strong",
    "volatility": "Medium",
    "liquidity": "High",
    "news_risk": "Low",
    "confidence": 91
}

summary = MarketSummary().generate_summary(market)

print(summary)