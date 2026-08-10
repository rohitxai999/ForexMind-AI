from pydantic import BaseModel, Field


class OpenTrade(BaseModel):
    risk_percent: float = Field(
        ...,
        ge=0,
        description="Risk percentage of an existing open trade.",
    )


class RiskEvaluationRequest(BaseModel):
    account_balance: float = Field(..., gt=0)
    risk_percent: float = Field(..., gt=0)
    entry_price: float = Field(..., gt=0)
    stop_loss: float = Field(..., gt=0)
    take_profit: float = Field(..., gt=0)

    open_trades: list[OpenTrade] = Field(default_factory=list)

    smc_score: float = Field(..., ge=0, le=100)
    ict_score: float = Field(..., ge=0, le=100)
    liquidity_score: float = Field(..., ge=0, le=100)
    ai_probability: float = Field(..., ge=0, le=100)
    risk_quality: float = Field(..., ge=0, le=100)
    risk_reward_score: float = Field(..., ge=0, le=100)

    daily_loss_percent: float = Field(
        default=0.0,
        ge=0,
    )

    pip_size: float = Field(
        default=0.0001,
        gt=0,
    )

    pip_value_per_lot: float = Field(
        default=10.0,
        gt=0,
    )
