from decimal import Decimal


class PositionSizingEngine:
    """
    Calculates position size based on account risk.

    Formula:
        Risk Amount = Account Balance * Risk %
        Position Size = Risk Amount / Stop Loss Risk
    """

    def calculate_risk_amount(
        self,
        account_balance: float,
        risk_percent: float,
    ) -> float:
        if account_balance <= 0:
            raise ValueError("Account balance must be greater than zero.")

        if risk_percent <= 0:
            raise ValueError("Risk percentage must be greater than zero.")

        return float(
            Decimal(str(account_balance))
            * Decimal(str(risk_percent))
            / Decimal("100")
        )

    def calculate_position_size(
        self,
        account_balance: float,
        risk_percent: float,
        entry_price: float,
        stop_loss: float,
        pip_size: float = 0.0001,
        pip_value_per_lot: float = 10.0,
    ) -> dict:
        if entry_price <= 0:
            raise ValueError("Entry price must be greater than zero.")

        if stop_loss <= 0:
            raise ValueError("Stop-loss price must be greater than zero.")

        if pip_size <= 0:
            raise ValueError("Pip size must be greater than zero.")

        if pip_value_per_lot <= 0:
            raise ValueError("Pip value must be greater than zero.")

        if entry_price == stop_loss:
            raise ValueError("Entry price and stop-loss cannot be equal.")

        risk_amount = self.calculate_risk_amount(
            account_balance,
            risk_percent,
        )

        stop_distance = abs(entry_price - stop_loss)

        stop_distance_pips = stop_distance / pip_size

        risk_per_lot = stop_distance_pips * pip_value_per_lot

        position_size = risk_amount / risk_per_lot

        return {
            "account_balance": round(account_balance, 2),
            "risk_percent": round(risk_percent, 4),
            "risk_amount": round(risk_amount, 2),
            "entry_price": entry_price,
            "stop_loss": stop_loss,
            "stop_distance": round(stop_distance, 6),
            "stop_distance_pips": round(stop_distance_pips, 2),
            "risk_per_lot": round(risk_per_lot, 2),
            "position_size_lots": round(position_size, 4),
        }
