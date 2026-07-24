from app.data.fetcher import get_forex_data
from app.analysis.indicators import calculate_indicators
from app.analysis.signals import generate_signal
from app.analysis.explanation import generate_explanation

df = get_forex_data("EURUSD=X")
df = calculate_indicators(df)

result = generate_signal(df)

print(generate_explanation(result))
