import pandas as pd
import numpy as np
from ta.trend import EMAIndicator, MACD, ADXIndicator
from ta.momentum import RSIIndicator, StochRSIIndicator
from ta.volatility import BollingerBands, AverageTrueRange


def calculate_indicators(df: pd.DataFrame):
    """
    Calculate technical indicators for ForexMind AI.
    """

    # Flatten multi-index columns if yfinance returns them
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Ensure required columns exist
    required_cols = ["Open", "High", "Low", "Close"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    close = df["Close"]
    high = df["High"]
    low = df["Low"]

    # ===== EMA =====
    df["EMA20"] = EMAIndicator(close=close, window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(close=close, window=50).ema_indicator()
    df["EMA200"] = EMAIndicator(close=close, window=200).ema_indicator()

    # ===== RSI =====
    df["RSI"] = RSIIndicator(close=close, window=14).rsi()

    # ===== MACD =====
    macd = MACD(close=close)
    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()
    df["MACD_HIST"] = macd.macd_diff()

    # ===== Bollinger Bands =====
    bb = BollingerBands(close=close, window=20, window_dev=2)
    df["BB_HIGH"] = bb.bollinger_hband()
    df["BB_LOW"] = bb.bollinger_lband()
    df["BB_MID"] = bb.bollinger_mavg()

    # ===== ATR =====
    atr = AverageTrueRange(high=high, low=low, close=close, window=14)
    df["ATR"] = atr.average_true_range()

    # ===== Stochastic RSI =====
    stoch = StochRSIIndicator(close=close, window=14)
    df["STOCH_RSI"] = stoch.stochrsi()

    # ===== ADX =====
    adx = ADXIndicator(high=high, low=low, close=close, window=14)
    df["ADX"] = adx.adx()

    return df


def get_latest_indicators(df: pd.DataFrame):
    """
    Return the latest indicator values as a dictionary.
    """
    latest = df.iloc[-1]

    return {
        "price": round(float(latest["Close"]), 5),
        "ema20": round(float(latest["EMA20"]), 5),
        "ema50": round(float(latest["EMA50"]), 5),
        "ema200": round(float(latest["EMA200"]), 5),
        "rsi": round(float(latest["RSI"]), 2),
        "macd": round(float(latest["MACD"]), 5),
        "macd_signal": round(float(latest["MACD_SIGNAL"]), 5),
        "macd_hist": round(float(latest["MACD_HIST"]), 5),
        "bb_high": round(float(latest["BB_HIGH"]), 5),
        "bb_low": round(float(latest["BB_LOW"]), 5),
        "atr": round(float(latest["ATR"]), 5),
        "stoch_rsi": round(float(latest["STOCH_RSI"]), 2),
        "adx": round(float(latest["ADX"]), 2),
    }