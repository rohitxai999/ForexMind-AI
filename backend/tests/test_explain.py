from app.ai.explain import ExplainableAI


features = {
    "trend": "Bullish",
    "rsi": 28,
    "macd": "Bullish",
    "volume": "High",
    "news": "Positive"
}

result = ExplainableAI.generate_explanation(
    features,
    prediction="BUY",
    probability=0.91
)

print("=" * 60)
print("ForexMind AI Explainable AI Test")
print("=" * 60)

print("\nPrediction:", result["prediction"])
print("Confidence:", result["confidence"], "%")

print("\nReasons:")

for reason in result["reasons"]:
    print("-", reason)