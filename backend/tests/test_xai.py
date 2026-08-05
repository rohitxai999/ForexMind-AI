from app.ai.explanation import ExplainableAI

xai = ExplainableAI()

report = xai.generate_report(
    prediction="BUY",
    confidence=91.5,
    indicators={
        "trend": "Bullish",
        "rsi": 45,
        "macd": 0.82,
        "volatility": 1.3
    }
)

print("=" * 60)
print("FOREXMIND AI - XAI REPORT")
print("=" * 60)

for key, value in report.items():
    print(f"{key}: {value}")