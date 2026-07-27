import numpy as np
import pandas as pd

from agents.coordinator import AgentCoordinator


# Generate 100 candle Forex sample data
close_prices = np.linspace(
    1.10,
    1.20,
    100
)


data = pd.DataFrame({

    "Open": close_prices - 0.001,

    "High": close_prices + 0.002,

    "Low": close_prices - 0.002,

    "Close": close_prices,

    "Volume": [1000] * 100

})


market_data = {

    "EURUSD=X": data

}


coordinator = AgentCoordinator()


result = coordinator.analyze_market(
    market_data
)


print("\n===== AGENT OUTPUT =====")

for agent in result["agents"]:
    print(agent)


print("\n===== RISK =====")
print(result["risk"])


print("\n===== DEBATE RESULT =====")
print(result["debate"])