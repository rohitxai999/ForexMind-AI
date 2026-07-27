class RiskAgent:
    """
    Determines risk level and recommended position size
    based on the final trading decision from Debate Agent.
    """


    def calculate_risk(self, decision):

        # Default values
        signal = "HOLD"
        confidence_value = 0


        # Handle dictionary input from Debate Agent
        if isinstance(decision, dict):

            signal = decision.get(
                "decision",
                "HOLD"
            )

            confidence_value = decision.get(
                "confidence",
                0
            )


        # Handle string input
        else:

            signal = decision



        # Convert confidence into category

        if isinstance(confidence_value, (int, float)):

            if confidence_value >= 70:

                confidence = "High"

            elif confidence_value >= 40:

                confidence = "Medium"

            else:

                confidence = "Low"

        else:

            confidence = confidence_value



        # BUY decision

        if signal == "BUY":

            if confidence == "High":

                return {

                    "decision": "BUY",

                    "risk": "Low",

                    "confidence": confidence,

                    "position_size": 1.00,

                    "stop_loss": "1.5%",

                    "take_profit": "3.0%",

                    "risk_reward_ratio": "1:2"

                }


            else:

                return {

                    "decision": "BUY",

                    "risk": "Medium",

                    "confidence": confidence,

                    "position_size": 0.75,

                    "stop_loss": "1.5%",

                    "take_profit": "2.5%",

                    "risk_reward_ratio": "1:1.7"

                }



        # SELL decision

        elif signal == "SELL":

            if confidence == "High":

                return {

                    "decision": "SELL",

                    "risk": "Low",

                    "confidence": confidence,

                    "position_size": 1.00,

                    "stop_loss": "1.5%",

                    "take_profit": "3.0%",

                    "risk_reward_ratio": "1:2"

                }


            else:

                return {

                    "decision": "SELL",

                    "risk": "Medium",

                    "confidence": confidence,

                    "position_size": 0.75,

                    "stop_loss": "1.5%",

                    "take_profit": "2.5%",

                    "risk_reward_ratio": "1:1.7"

                }



        # HOLD decision

        return {

            "decision": "HOLD",

            "risk": "High",

            "confidence": confidence,

            "position_size": 0.00,

            "stop_loss": "N/A",

            "take_profit": "N/A",

            "risk_reward_ratio": "N/A"

        }