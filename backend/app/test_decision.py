from app.agents.decision.decision_agent import DecisionAgent

agent = DecisionAgent()

result = agent.make_decision(
    buy_probability=82,
    sell_probability=12,
    neutral_probability=6,
)

print("Decision Agent Test")
print("-" * 30)
print(result)