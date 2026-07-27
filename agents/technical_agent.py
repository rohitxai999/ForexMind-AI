from services.indicators import calculate_indicators


class TechnicalAgent:

    def __init__(self):
        self.name = "Technical Agent"


    def analyze(self, market_data):

        results = []

        for symbol, df in market_data.items():

            # Calculate indicators
            df = calculate_indicators(df)

            # Latest candle
            latest = df.iloc[-1]

            signal = self.generate_signal(latest)


            # Convert STRONG BUY/SELL into normal signals
            decision = signal["decision"]

            if "BUY" in decision:
                final_signal = "BUY"

            elif "SELL" in decision:
                final_signal = "SELL"

            else:
                final_signal = "HOLD"


            results.append({

                "agent": self.name,

                "symbol": symbol,

                "signal": final_signal,

                "confidence": signal["confidence"],

                "reason":
                f"Technical indicators generated {decision}",

                "details": {

                    "score": signal["score"],

                    "original_decision": decision

                }

            })


        return results



    def generate_signal(self, row):

        score = 0


        # RSI
        if row["RSI"] < 30:
            score += 2

        elif row["RSI"] > 70:
            score -= 2


        # EMA Trend
        if row["EMA20"] > row["EMA50"]:
            score += 1

        else:
            score -= 1


        # MACD
        if row["MACD"] > row["MACD_SIGNAL"]:
            score += 1

        else:
            score -= 1



        if score >= 3:

            decision = "STRONG BUY"

        elif score >= 1:

            decision = "BUY"

        elif score == 0:

            decision = "HOLD"

        elif score <= -3:

            decision = "STRONG SELL"

        else:

            decision = "SELL"



        confidence = min(abs(score) * 25, 100)


        return {

            "decision": decision,

            "score": score,

            "confidence": confidence

        }