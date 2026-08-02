from app.services.explainability.explanation_engine import ExplanationEngine

engine = ExplanationEngine()

result = engine.generate(
    action="BUY",
    confidence=88,
    risk="LOW",
    rsi=25,
    macd_signal="BUY",
    ema_signal="BUY",
    news_sentiment="POSITIVE",
)

print(result)