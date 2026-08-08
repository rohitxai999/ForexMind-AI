from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.trading.analytics import TradeAnalytics
from app.trading.models import Trade
from app.trading.trade_manager import TradeManager


router = APIRouter(
    prefix="/trades",
    tags=["Trading"],
)

trade_manager = TradeManager()


class TradeRequest(BaseModel):
    pair: str
    direction: str
    entry_price: float = Field(gt=0)
    stop_loss: float = Field(gt=0)
    take_profit: float = Field(gt=0)
    position_size: float = Field(gt=0)
    risk_percent: float = Field(ge=0)
    smc_setup: Optional[str] = None
    ict_setup: Optional[str] = None
    liquidity_event: Optional[str] = None
    confidence: Optional[float] = Field(default=None, ge=0, le=100)


class CloseTradeRequest(BaseModel):
    result: str
    pnl: float


@router.post("/")
def create_trade(request: TradeRequest):
    try:
        trade = Trade(
            pair=request.pair,
            direction=request.direction,
            entry_price=request.entry_price,
            stop_loss=request.stop_loss,
            take_profit=request.take_profit,
            position_size=request.position_size,
            risk_percent=request.risk_percent,
            smc_setup=request.smc_setup,
            ict_setup=request.ict_setup,
            liquidity_event=request.liquidity_event,
            confidence=request.confidence,
        )

        created_trade = trade_manager.create_trade(trade)

        return {
            "success": True,
            "trade": created_trade,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@router.get("/")
def list_trades():
    trades = trade_manager.list_trades()

    return {
        "success": True,
        "count": len(trades),
        "trades": trades,
    }


@router.get("/open")
def open_trades():
    trades = trade_manager.get_open_trades()

    return {
        "success": True,
        "count": len(trades),
        "trades": trades,
    }


@router.get("/closed")
def closed_trades():
    trades = trade_manager.get_closed_trades()

    return {
        "success": True,
        "count": len(trades),
        "trades": trades,
    }


@router.get("/analytics/summary")
def analytics_summary():
    analytics = TradeAnalytics(
        trade_manager.list_trades()
    )

    return {
        "success": True,
        "analytics": analytics.summary(),
    }


@router.get("/analytics/strategy")
def strategy_analytics():
    analytics = TradeAnalytics(
        trade_manager.list_trades()
    )

    return {
        "success": True,
        "strategy_performance": analytics.strategy_performance(),
    }


@router.get("/{trade_id}")
def get_trade(trade_id: str):
    trade = trade_manager.get_trade(trade_id)

    if trade is None:
        raise HTTPException(
            status_code=404,
            detail="Trade not found",
        )

    return {
        "success": True,
        "trade": trade,
    }


@router.post("/{trade_id}/close")
def close_trade(
    trade_id: str,
    request: CloseTradeRequest,
):
    try:
        trade = trade_manager.close_trade(
            trade_id=trade_id,
            result=request.result,
            pnl=request.pnl,
        )

        return {
            "success": True,
            "trade": trade,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )
