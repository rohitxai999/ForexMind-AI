class RiskAgent:
    """
    Determines risk level and recommended position size
    based on the final trading decision.
    """

    def calculate_risk(self, decision):

        # Handle both dictionary and string inputs
        if isinstance(decision, dict):
            signal = decision.get("decision", "HOLD")
            confidence = decision.get("confidence", "Low")
        else:
            signal = decision
            confidence = "Low"

        if signal == "BUY":
            if confidence == "High":
                return {
                    "risk": "Low",
                    "position_size": 1.00,
                    "stop_loss": "1.5%",
                    "take_profit": "3.0%",
                    "risk_reward_ratio": "1:2"
                }
            else:
                return {
                    "risk": "Medium",
                    "position_size": 0.75,
                    "stop_loss": "1.5%",
                    "take_profit": "2.5%",
                    "risk_reward_ratio": "1:1.7"
                }

        elif signal == "SELL":
            if confidence == "High":
                return {
                    "risk": "Low",
                    "position_size": 1.00,
                    "stop_loss": "1.5%",
                    "take_profit": "3.0%",
                    "risk_reward_ratio": "1:2"
                }
            else:
                return {
                    "risk": "Medium",
                    "position_size": 0.75,
                    "stop_loss": "1.5%",
                    "take_profit": "2.5%",
                    "risk_reward_ratio": "1:1.7"
                }

        return {
            "risk": "High",
            "position_size": 0.00,
            "stop_loss": "N/A",
            "take_profit": "N/A",
            "risk_reward_ratio": "N/A"
        }