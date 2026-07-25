class RiskAgent:

    def calculate_risk(self, signal):

        if signal == "BUY":
            return {
                "risk": "Low",
                "position_size": 1.0
            }

        elif signal == "SELL":
            return {
                "risk": "Medium",
                "position_size": 0.8
            }

        return {
            "risk": "High",
            "position_size": 0
        }