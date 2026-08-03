class MarketRegimeEngine:

    def __init__(self):
        self.atr_threshold = 2.0

    def calculate_volatility(self, atr):
        return "HIGH" if atr >= self.atr_threshold else "LOW"

    def calculate_trend(self, ema_signal, adx):
        if ema_signal == "BUY" and adx > 25:
            return "UPTREND"

        if ema_signal == "SELL" and adx > 25:
            return "DOWNTREND"

        return "SIDEWAYS"

    def get_market_state(self, ema_signal, adx, atr, rsi):

        volatility = self.calculate_volatility(atr)
        trend = self.calculate_trend(ema_signal, adx)

        if trend == "UPTREND" and rsi > 55:
            return "BULLISH_TREND"

        if trend == "DOWNTREND" and rsi < 45:
            return "BEARISH_TREND"

        if adx < 20:
            return "SIDEWAYS"

        if volatility == "HIGH":
            return "HIGH_VOLATILITY"

        return "LOW_VOLATILITY"

    def detect(self, ema_signal, adx, atr, rsi):

        return {
            "market_state": self.get_market_state(
                ema_signal,
                adx,
                atr,
                rsi
            )
        }