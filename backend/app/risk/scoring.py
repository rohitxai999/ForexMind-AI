class TradeQualityScorer:
    """
    Calculates a 0-100 trade quality score.

    Inputs are expected to be normalized between 0 and 100.
    """

    WEIGHTS = {
        "smc_score": 0.20,
        "ict_score": 0.20,
        "liquidity_score": 0.20,
        "ai_probability": 0.20,
        "risk_quality": 0.10,
        "risk_reward_score": 0.10,
    }

    def _validate_score(self, name: str, value: float) -> float:
        if value < 0 or value > 100:
            raise ValueError(
                f"{name} must be between 0 and 100."
            )

        return float(value)

    def calculate(
        self,
        smc_score: float,
        ict_score: float,
        liquidity_score: float,
        ai_probability: float,
        risk_quality: float,
        risk_reward_score: float,
    ) -> dict:

        scores = {
            "smc_score": self._validate_score(
                "SMC score",
                smc_score,
            ),
            "ict_score": self._validate_score(
                "ICT score",
                ict_score,
            ),
            "liquidity_score": self._validate_score(
                "Liquidity score",
                liquidity_score,
            ),
            "ai_probability": self._validate_score(
                "AI probability",
                ai_probability,
            ),
            "risk_quality": self._validate_score(
                "Risk quality",
                risk_quality,
            ),
            "risk_reward_score": self._validate_score(
                "Risk/reward score",
                risk_reward_score,
            ),
        }

        weighted_score = sum(
            scores[name] * weight
            for name, weight in self.WEIGHTS.items()
        )

        score = round(weighted_score, 2)

        if score >= 85:
            quality = "HIGH"
            recommendation = "APPROVE"

        elif score >= 70:
            quality = "MEDIUM"
            recommendation = "REDUCE_RISK"

        else:
            quality = "LOW"
            recommendation = "REJECT"

        return {
            "score": score,
            "quality": quality,
            "recommendation": recommendation,
            "components": scores,
            "weights": self.WEIGHTS.copy(),
        }
