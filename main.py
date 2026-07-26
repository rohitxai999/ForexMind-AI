from agents.coordinator import Coordinator


def main():

    bot = Coordinator()

    results = bot.run()

    for pair, info in results.items():

        print("=" * 70)
        print(f"Currency Pair : {pair}")

        print("\n📊 Technical Analysis")
        print(
            "Signal       :",
            info["technical"]["decision"]
        )

        print(
            "Score        :",
            info["technical"]["score"]
        )

        print(
            "Confidence   :",
            info["technical"]["confidence"]
        )


        print("\n📰 Market Sentiment")

        print(
            "Overall      :",
            info["sentiment"]["overall_sentiment"]
        )

        print(
            "Average Score:",
            info["sentiment"]["average_score"]
        )


        print("\n🤖 AI Decision")

        print(
            "Decision     :",
            info["decision"]["decision"]
        )

        print(
            "Confidence   :",
            info["decision"]["confidence"]
        )

        print(
            "Reason       :",
            info["decision"]["reason"]
        )


        print("\n🛡️ Risk Management")

        print(
            "Risk Level   :",
            info["risk"]["risk"]
        )

        print(
            "Position Size:",
            info["risk"]["position_size"]
        )

        print(
            "Stop Loss    :",
            info["risk"]["stop_loss"]
        )

        print(
            "Take Profit  :",
            info["risk"]["take_profit"]
        )

        print(
            "Risk Reward  :",
            info["risk"]["risk_reward_ratio"]
        )


        print("=" * 70)


if __name__ == "__main__":
    main()