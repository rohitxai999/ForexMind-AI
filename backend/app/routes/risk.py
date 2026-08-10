from fastapi import APIRouter

from app.risk.engine import RiskEngine
from app.schemas.risk import RiskEvaluationRequest


router = APIRouter(
    prefix="/risk",
    tags=["Risk Management"],
)

risk_engine = RiskEngine()


@router.post("/evaluate")
def evaluate_risk(request: RiskEvaluationRequest):
    open_trades = [
        trade.model_dump()
        for trade in request.open_trades
    ]

    return risk_engine.evaluate_trade(
        account_balance=request.account_balance,
        risk_percent=request.risk_percent,
        entry_price=request.entry_price,
        stop_loss=request.stop_loss,
        take_profit=request.take_profit,
        open_trades=open_trades,
        smc_score=request.smc_score,
        ict_score=request.ict_score,
        liquidity_score=request.liquidity_score,
        ai_probability=request.ai_probability,
        risk_quality=request.risk_quality,
        risk_reward_score=request.risk_reward_score,
        daily_loss_percent=request.daily_loss_percent,
        pip_size=request.pip_size,
        pip_value_per_lot=request.pip_value_per_lot,
    )
