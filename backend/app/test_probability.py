from app.services.probability.probability_engine import ProbabilityEngine

engine = ProbabilityEngine()

result = engine.calculate(
    rsi=25,
    macd_signal="BUY",
    ema_signal="BUY",
    news_sentiment="POSITIVE",
)

print("Probability Engine Test")
print("-" * 30)
print(result)