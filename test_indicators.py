from app.data.fetcher import get_forex_data
from app.analysis.indicators import calculate_indicators

df = get_forex_data("EURUSD=X")

df = calculate_indicators(df)

print(df.tail())