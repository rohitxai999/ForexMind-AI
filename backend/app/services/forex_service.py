import pandas as pd
import yfinance as yf


class ForexService:

    def get_market_data(self, pair: str):
        symbol = pair.replace("/", "") + "=X"

        df = yf.download(
            symbol,
            period="3mo",
            interval="1h",
            auto_adjust=False,
            progress=False,
        )

        if df.empty:
            raise ValueError(f"No market data found for {pair}")

        # Flatten MultiIndex columns (latest yfinance)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Keep only the required columns
        df = df[["Open", "High", "Low", "Close", "Volume"]]

        # Ensure all values are numeric
        df = df.apply(pd.to_numeric, errors="coerce")

        # Remove rows with missing values
        df = df.dropna()

        return df