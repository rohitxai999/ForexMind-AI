from agents.coordinator import Coordinator


def main():

    bot = Coordinator()

    results = bot.run()

    for pair, info in results.items():

        print("=" * 60)
        print(pair)

        print(
            "Technical Signal :",
            info["technical"]["decision"]
        )

        print(
            "Score            :",
            info["technical"]["score"]
        )

        print(
            "Confidence       :",
            info["technical"]["confidence"]
        )

        print(
            "Sentiment        :",
            info["sentiment"]
        )

        print(
            "Final Decision   :",
            info["decision"]
        )

        print(
            "Risk             :",
            info["risk"]["risk"]
        )

        print(
            "Position Size    :",
            info["risk"]["position_size"]
        )


if __name__ == "__main__":
    main()