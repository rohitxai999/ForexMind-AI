from config.risk_config import (
    MAX_RISK_PERCENT,
    RISK_REWARD_RATIO,
    DEFAULT_PIP_VALUE
)


class RiskAgent:

    def calculate_position_size(
        self,
        account_balance,
        stop_loss_pips,
        pip_value=DEFAULT_PIP_VALUE
    ):

        risk_amount = account_balance * (MAX_RISK_PERCENT / 100)

        lot_size = risk_amount / (stop_loss_pips * pip_value)

        return round(lot_size, 2)

    def calculate_trade_levels(self, entry_price, stop_loss_pips):

        sl = entry_price - (stop_loss_pips * 0.0001)

        tp = entry_price + (
            stop_loss_pips *
            RISK_REWARD_RATIO *
            0.0001
        )

        return {
            "stop_loss": round(sl, 5),
            "take_profit": round(tp, 5)
        }