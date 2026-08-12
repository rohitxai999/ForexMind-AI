from app.analysis.liquidity.interpreter import LiquidityInterpreter
from app.analysis.liquidity.liquidity_engine import LiquidityEngine
from app.services.forex_service import ForexService
from app.services.indicator_service import IndicatorService
import pandas as pd


class MarketAgent:

    def __init__(self):
        self.forex = ForexService()
        self.indicator = IndicatorService()
        self.liquidity = LiquidityEngine()
        self.liquidity_interpreter = LiquidityInterpreter()

    def analyze(self, pair: str):

        df = self.forex.get_market_data(pair)

        # Flatten MultiIndex columns if present
        if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
            df.columns = df.columns.get_level_values(0)

        indicators = self.indicator.calculate(df)

        close = df["Close"]

        # Convert DataFrame column to Series if needed
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        latest_price = float(close.iloc[-1])

        candles = self._prepare_candles(df)

        liquidity_analysis = self.liquidity.analyze(candles)

        liquidity_context = self.liquidity_interpreter.interpret(
            liquidity_analysis
        )

        return {
            "pair": pair,
            "price": round(latest_price, 5),
            "trend": indicators["trend"],
            "rsi": indicators["rsi"],
            "ema20": indicators["ema20"],
            "ema50": indicators["ema50"],
            "macd": indicators["macd"],
            "signal": indicators["signal"],
            "liquidity": self._format_liquidity_analysis(
                liquidity_analysis
            ),
            "liquidity_context": {
                "bias": liquidity_context.bias,
                "event": liquidity_context.event,
                "explanation": liquidity_context.explanation,
                "confidence_contribution": (
                    liquidity_context.confidence_contribution
                ),
            },
        }

    def _prepare_candles(self, df: pd.DataFrame) -> list[dict]:
        candles = []

        for _, row in df.iterrows():
            candles.append(
                {
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                }
            )

        return candles

    def _format_liquidity_analysis(self, analysis) -> dict:
        return {
            "buy_side_count": len(
                analysis.buy_side_liquidity
            ),
            "sell_side_count": len(
                analysis.sell_side_liquidity
            ),
            "sweep_count": len(
                analysis.sweeps
            ),
            "buy_side": [
                {
                    "price": pool.price,
                    "type": pool.pool_type.value,
                    "strength": pool.strength,
                    "index": pool.index,
                }
                for pool in analysis.buy_side_liquidity
            ],
            "sell_side": [
                {
                    "price": pool.price,
                    "type": pool.pool_type.value,
                    "strength": pool.strength,
                    "index": pool.index,
                }
                for pool in analysis.sell_side_liquidity
            ],
            "sweeps": [
                {
                    "price": sweep.price,
                    "type": sweep.liquidity_type.value,
                    "direction": sweep.direction.value,
                    "index": sweep.index,
                    "confirmation": sweep.confirmation,
                }
                for sweep in analysis.sweeps
            ],
        }
