import yfinance as yf
import pandas as pd


def get_forex_data(symbol):
    # Download forex data
    data = yf.download(
        tickers=symbol,
        period="5d",
        interval="1h",
        auto_adjust=False,
        progress=False,
    )

    # Handle MultiIndex columns returned by newer yfinance versions
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Keep only the columns we need
    data = data[["Open", "High", "Low", "Close", "Volume"]]

    return data