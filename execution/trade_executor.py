from datetime import datetime


class TradeExecutor:

    def open_trade(
        self,
        symbol,
        decision,
        entry,
        stop_loss,
        take_profit,
        lot_size
    ):

        trade = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "symbol": symbol,
            "decision": decision,
            "entry": entry,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "lot_size": lot_size,
            "status": "OPEN"
        }

        return trade