from agents.multi_timeframe_agent import multi_timeframe_agent

sample = {
    "M5": "BUY",
    "M15": "BUY",
    "H1": "BUY",
    "H4": "HOLD",
}

result = multi_timeframe_agent.analyze(sample)

print("=" * 60)
print(result)
print("=" * 60)