import yfinance as yf
import pandas as pd


def get_forex_data(symbol="EURUSD=X", period="3mo", interval="1h"):
    """
    Download Forex market data from Yahoo Finance.
    """

    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        progress=False,
        auto_adjust=False,
    )

    if df.empty:
        raise Exception(f"No data found for {symbol}")

    # Handle MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Keep only required columns
    required = ["Open", "High", "Low", "Close"]

    for col in required:
        if col not in df.columns:
            raise Exception(f"Missing column: {col}")

    return df