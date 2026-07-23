from services.indicators import calculate_indicators


class TechnicalAgent:

    def analyze(self, market_data):

        result = {}

        for symbol, df in market_data.items():

            df = calculate_indicators(df)

            latest = df.iloc[-1]

            signal = self.generate_signal(latest)

            result[symbol] = {
                "data": df,
                "signal": signal
            }

        return result

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