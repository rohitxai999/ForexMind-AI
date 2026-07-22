import pandas as pd
from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator


class IndicatorService:

    def calculate(self, df):
        # Get the Close column
        close = df["Close"]

        # Convert DataFrame column to Series if needed
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        # Ensure numeric values
        close = pd.to_numeric(close, errors="coerce")

        # Remove missing values
        close = close.dropna()

        # Calculate indicators
        ema20 = EMAIndicator(close=close, window=20).ema_indicator()
        ema50 = EMAIndicator(close=close, window=50).ema_indicator()
        rsi = RSIIndicator(close=close, window=14).rsi()
        macd = MACD(close=close).macd()

        # Determine trend
        trend = "Bullish" if ema20.iloc[-1] > ema50.iloc[-1] else "Bearish"

        # Generate signal
        if rsi.iloc[-1] < 30:
            signal = "BUY"
        elif rsi.iloc[-1] > 70:
            signal = "SELL"
        else:
            signal = "HOLD"

        return {
            "trend": trend,
            "ema20": round(float(ema20.iloc[-1]), 5),
            "ema50": round(float(ema50.iloc[-1]), 5),
            "rsi": round(float(rsi.iloc[-1]), 2),
            "macd": round(float(macd.iloc[-1]), 5),
            "signal": signal,
        }