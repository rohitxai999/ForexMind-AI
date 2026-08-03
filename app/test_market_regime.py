from app.services.market_regime.regime_engine import MarketRegimeEngine


engine = MarketRegimeEngine()

print("=" * 40)
print("Market Regime Detection Test")
print("=" * 40)

tests = [
    {
        "name": "Bullish Trend",
        "input": {
            "ema_signal": "BUY",
            "adx": 30,
            "atr": 2.5,
            "rsi": 65
        }
    },
    {
        "name": "Bearish Trend",
        "input": {
            "ema_signal": "SELL",
            "adx": 32,
            "atr": 3.1,
            "rsi": 35
        }
    },
    {
        "name": "Sideways",
        "input": {
            "ema_signal": "BUY",
            "adx": 15,
            "atr": 1.2,
            "rsi": 50
        }
    },
    {
        "name": "High Volatility",
        "input": {
            "ema_signal": "BUY",
            "adx": 22,
            "atr": 3.0,
            "rsi": 50
        }
    },
    {
        "name": "Low Volatility",
        "input": {
            "ema_signal": "BUY",
            "adx": 22,
            "atr": 1.0,
            "rsi": 50
        }
    }
]

for test in tests:
    print(f"\n{test['name']}")
    result = engine.detect(**test["input"])
    print(result)