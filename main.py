from agents.coordinator import Coordinator


def main():

    bot = Coordinator()

    result = bot.run()

    for pair, info in result.items():

        print("=" * 60)
        print(pair)

        signal = info["signal"]

        print(f"Decision    : {signal['decision']}")
        print(f"Score       : {signal['score']}")
        print(f"Confidence  : {signal['confidence']}%")

        latest = info["data"].iloc[-1]

        print(f"Price       : {latest['Close']:.5f}")
        print(f"RSI         : {latest['RSI']:.2f}")
        print(f"EMA20       : {latest['EMA20']:.5f}")
        print(f"EMA50       : {latest['EMA50']:.5f}")
        print(f"MACD        : {latest['MACD']:.5f}")

        print()

if __name__ == "__main__":
    main()