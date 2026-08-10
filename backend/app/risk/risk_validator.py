class RiskValidator:
    """
    Validates whether a trade satisfies ForexMind risk rules.
    """

    def __init__(
        self,
        max_risk_percent: float = 2.0,
        min_risk_reward: float = 1.5,
        max_daily_loss_percent: float = 5.0,
    ):
        self.max_risk_percent = max_risk_percent
        self.min_risk_reward = min_risk_reward
        self.max_daily_loss_percent = max_daily_loss_percent

    def validate(
        self,
        account_balance: float,
        risk_percent: float,
        entry_price: float,
        stop_loss: float,
        take_profit: float,
        daily_loss_percent: float = 0.0,
        position_size: float = 0.0,
    ) -> dict:

        errors = []
        warnings = []

        if account_balance <= 0:
            errors.append("Account balance must be greater than zero.")

        if risk_percent <= 0:
            errors.append("Risk percentage must be greater than zero.")

        if risk_percent > self.max_risk_percent:
            errors.append(
                f"Risk exceeds maximum allowed risk of "
                f"{self.max_risk_percent}%."
            )

        if entry_price <= 0:
            errors.append("Entry price must be greater than zero.")

        if stop_loss <= 0:
            errors.append("Stop-loss must be greater than zero.")

        if take_profit <= 0:
            errors.append("Take-profit must be greater than zero.")

        if position_size <= 0:
            errors.append("Position size must be greater than zero.")

        if entry_price == stop_loss:
            errors.append("Entry price and stop-loss cannot be equal.")

        if entry_price == take_profit:
            errors.append("Entry price and take-profit cannot be equal.")

        if daily_loss_percent < 0:
            errors.append("Daily loss cannot be negative.")

        if daily_loss_percent >= self.max_daily_loss_percent:
            errors.append(
                f"Daily loss has reached the maximum allowed limit "
                f"of {self.max_daily_loss_percent}%."
            )

        if not errors:
            stop_distance = abs(entry_price - stop_loss)
            target_distance = abs(take_profit - entry_price)

            risk_reward = target_distance / stop_distance

            if risk_reward < self.min_risk_reward:
                errors.append(
                    f"Risk/reward ratio {risk_reward:.2f} is below "
                    f"minimum required ratio of {self.min_risk_reward:.2f}."
                )

            if risk_reward >= 2.0:
                warnings.append("Strong risk/reward setup.")

            if risk_percent <= 1.0:
                warnings.append("Conservative trade risk.")

        approved = len(errors) == 0

        return {
            "approved": approved,
            "status": "APPROVED" if approved else "REJECTED",
            "risk_percent": round(risk_percent, 4),
            "daily_loss_percent": round(daily_loss_percent, 4),
            "risk_reward": (
                round(risk_reward, 2)
                if not errors and "risk_reward" in locals()
                else None
            ),
            "errors": errors,
            "warnings": warnings,
        }
