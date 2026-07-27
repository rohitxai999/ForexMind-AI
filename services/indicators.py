import ta


def calculate_indicators(df):

    # Copy dataframe
    df = df.copy()


    # Ensure required column exists
    if "Close" not in df.columns:
        raise ValueError(
            "Market data must contain 'Close' column"
        )


    # EMA indicators
    df["EMA20"] = ta.trend.ema_indicator(
        df["Close"],
        window=20
    )

    df["EMA50"] = ta.trend.ema_indicator(
        df["Close"],
        window=50
    )


    # RSI indicator
    df["RSI"] = ta.momentum.rsi(
        df["Close"],
        window=14
    )


    # MACD indicators
    macd = ta.trend.MACD(
        df["Close"]
    )


    df["MACD"] = macd.macd()

    df["MACD_SIGNAL"] = macd.macd_signal()


    # Remove incomplete rows after indicators
    df = df.dropna()


    return df