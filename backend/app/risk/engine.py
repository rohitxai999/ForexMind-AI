from app.risk.position_sizing import PositionSizingEngine
from app.risk.risk_validator import RiskValidator
from app.risk.exposure import ExposureManager
from app.risk.scoring import TradeQualityScorer


class RiskEngine:
    """
    Central risk intelligence engine for ForexMind AI.

    Combines:
    - Position sizing
    - Risk validation
    - Portfolio exposure
    - Trade quality scoring
    """

    def __init__(
        self,
        max_risk_percent: float = 2.0,
        min_risk_reward: float = 1.5,
        max_daily_loss_percent: float = 5.0,
        max_total_risk_percent: float = 5.0,
        max_open_positions: int = 5,
    ):
        self.position_sizer = PositionSizingEngine()

        self.risk_validator = RiskValidator(
            max_risk_percent=max_risk_percent,
            min_risk_reward=min_risk_reward,
            max_daily_loss_percent=max_daily_loss_percent,
        )

        self.exposure_manager = ExposureManager(
            max_total_risk_percent=max_total_risk_percent,
            max_open_positions=max_open_positions,
        )

        self.scorer = TradeQualityScorer()

    def evaluate_trade(
        self,
        account_balance: float,
        risk_percent: float,
        entry_price: float,
        stop_loss: float,
        take_profit: float,
        open_trades: list,
        smc_score: float,
        ict_score: float,
        liquidity_score: float,
        ai_probability: float,
        risk_quality: float,
        risk_reward_score: float,
        daily_loss_percent: float = 0.0,
        pip_size: float = 0.0001,
        pip_value_per_lot: float = 10.0,
    ) -> dict:

        position = self.position_sizer.calculate_position_size(
            account_balance=account_balance,
            risk_percent=risk_percent,
            entry_price=entry_price,
            stop_loss=stop_loss,
            pip_size=pip_size,
            pip_value_per_lot=pip_value_per_lot,
        )

        validation = self.risk_validator.validate(
            account_balance=account_balance,
            risk_percent=risk_percent,
            entry_price=entry_price,
            stop_loss=stop_loss,
            take_profit=take_profit,
            daily_loss_percent=daily_loss_percent,
            position_size=position["position_size_lots"],
        )

        exposure = self.exposure_manager.validate_exposure(
            open_trades=open_trades,
            new_trade_risk_percent=risk_percent,
        )

        quality = self.scorer.calculate(
            smc_score=smc_score,
            ict_score=ict_score,
            liquidity_score=liquidity_score,
            ai_probability=ai_probability,
            risk_quality=risk_quality,
            risk_reward_score=risk_reward_score,
        )

        reasons = []
        decision = "APPROVE"

        if not validation["approved"]:
            decision = "REJECT"
            reasons.extend(validation["errors"])

        if not exposure["approved"]:
            decision = "REJECT"
            reasons.extend(exposure["errors"])

        if quality["recommendation"] == "REJECT":
            decision = "REJECT"
            reasons.append(
                "Trade quality score is below the minimum threshold."
            )

        elif (
            quality["recommendation"] == "REDUCE_RISK"
            and decision == "APPROVE"
        ):
            decision = "REDUCE_RISK"
            reasons.append(
                "Trade quality is acceptable but risk should be reduced."
            )

        if not reasons:
            reasons.append(
                "Trade passed risk, exposure, and quality checks."
            )

        return {
            "decision": decision,
            "position": position,
            "risk_validation": validation,
            "exposure": exposure,
            "quality": quality,
            "reasons": reasons,
        }
