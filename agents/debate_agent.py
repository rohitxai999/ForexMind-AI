from agents.base_agent import BaseAgent


class DebateAgent(BaseAgent):

    def __init__(self):
        super().__init__("Debate Agent")


    def analyze(self, agent_outputs):

        buy_score = 0
        sell_score = 0
        hold_score = 0


        votes = []


        for result in agent_outputs:


            # Technical / Prediction / Strategy agents
            if "signal" in result:

                signal = result.get(
                    "signal",
                    "HOLD"
                )

                confidence = result.get(
                    "confidence",
                    0
                )


            # Sentiment Agent conversion
            elif "overall_sentiment" in result:

                sentiment = result.get(
                    "overall_sentiment",
                    "Neutral"
                )


                if sentiment == "Positive":

                    signal = "BUY"
                    confidence = abs(
                        result.get(
                            "average_score",
                            0
                        )
                    ) * 100


                elif sentiment == "Negative":

                    signal = "SELL"
                    confidence = abs(
                        result.get(
                            "average_score",
                            0
                        )
                    ) * 100


                else:

                    signal = "HOLD"
                    confidence = 20


            else:

                continue



            confidence = round(
                float(confidence),
                2
            )


            if signal == "BUY":

                buy_score += confidence


            elif signal == "SELL":

                sell_score += confidence


            else:

                hold_score += confidence



            votes.append({

                "agent":
                result.get(
                    "agent",
                    result.get(
                        "pair",
                        "Unknown"
                    )
                ),

                "signal": signal,

                "confidence": confidence

            })



        scores = {

            "BUY": buy_score,

            "SELL": sell_score,

            "HOLD": hold_score

        }



        decision = max(
            scores,
            key=scores.get
        )


        total = sum(
            scores.values()
        )


        confidence = 0


        if total > 0:

            confidence = round(
                (scores[decision] / total) * 100,
                2
            )



        return {

            "decision": decision,

            "confidence": confidence,

            "agent_votes": scores,

            "votes": votes,

            "reason":
            "Decision based on multi-agent agreement"

        }