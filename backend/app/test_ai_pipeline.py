from app.services.probability.probability_engine import ProbabilityEngine
from app.agents.decision.decision_agent import DecisionAgent
from app.services.explainability.explanation_engine import ExplanationEngine


probability_engine = ProbabilityEngine()
decision_agent = DecisionAgent()
explanation_engine = ExplanationEngine()


# Example market inputs
rsi = 25
macd_signal = "BUY"
ema_signal = "BUY"
news_sentiment = "POSITIVE"

# Step 1: Calculate probabilities
probabilities = probability_engine.calculate(
    rsi=rsi,
    macd_signal=macd_signal,
    ema_signal=ema_signal,
    news_sentiment=news_sentiment,
)

# Step 2: Make a decision
decision = decision_agent.make_decision(
    buy_probability=probabilities["buy_probability"],
    sell_probability=probabilities["sell_probability"],
    neutral_probability=probabilities["neutral_probability"],
)

# Step 3: Generate explanation
report = explanation_engine.generate(
    action=decision["action"],
    confidence=decision["confidence"],
    risk=decision["risk"],
    rsi=rsi,
    macd_signal=macd_signal,
    ema_signal=ema_signal,
    news_sentiment=news_sentiment,
)

print("=" * 60)
print("FOREXMIND AI - COMPLETE PIPELINE")
print("=" * 60)
print()
print("Probabilities:")
print(probabilities)
print()
print("Decision:")
print(decision)
print()
print(report)
print("=" * 60)