class ExposureManager:
    """
    Tracks and validates total trading exposure.
    """

    def __init__(
        self,
        max_total_risk_percent: float = 5.0,
        max_open_positions: int = 5,
    ):
        self.max_total_risk_percent = max_total_risk_percent
        self.max_open_positions = max_open_positions

    def calculate_total_risk(
        self,
        open_trades: list,
    ) -> float:
        return round(
            sum(
                float(trade.get("risk_percent", 0.0))
                for trade in open_trades
            ),
            4,
        )

    def validate_exposure(
        self,
        open_trades: list,
        new_trade_risk_percent: float,
    ) -> dict:

        current_positions = len(open_trades)

        current_risk = self.calculate_total_risk(open_trades)

        projected_risk = round(
            current_risk + new_trade_risk_percent,
            4,
        )

        errors = []
        warnings = []

        if current_positions >= self.max_open_positions:
            errors.append(
                f"Maximum open positions limit of "
                f"{self.max_open_positions} reached."
            )

        if projected_risk > self.max_total_risk_percent:
            errors.append(
                f"Total projected risk of {projected_risk}% "
                f"exceeds maximum allowed risk of "
                f"{self.max_total_risk_percent}%."
            )

        if projected_risk >= self.max_total_risk_percent * 0.8:
            warnings.append(
                "Total portfolio risk is approaching the maximum limit."
            )

        approved = len(errors) == 0

        return {
            "approved": approved,
            "status": "APPROVED" if approved else "REJECTED",
            "open_positions": current_positions,
            "current_risk_percent": current_risk,
            "new_trade_risk_percent": round(
                new_trade_risk_percent,
                4,
            ),
            "projected_risk_percent": projected_risk,
            "max_total_risk_percent": self.max_total_risk_percent,
            "max_open_positions": self.max_open_positions,
            "errors": errors,
            "warnings": warnings,
        }
