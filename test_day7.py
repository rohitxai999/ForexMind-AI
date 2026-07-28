from agents.risk_agent import RiskAgent
from agents.consensus_agent import ConsensusAgent
from execution.trade_executor import TradeExecutor
from database.trade_db import TradeDatabase
from journal.performance import PerformanceAnalytics


def main():

    # ----------------------------
    # Initialize
    # ----------------------------
    risk = RiskAgent()
    consensus = ConsensusAgent()
    executor = TradeExecutor()
    db = TradeDatabase()

    # ----------------------------
    # Risk Calculation
    # ----------------------------
    lot = risk.calculate_position_size(
        account_balance=100000,
        stop_loss_pips=25
    )

    levels = risk.calculate_trade_levels(
        entry_price=1.17120,
        stop_loss_pips=25
    )

    # ----------------------------
    # Consensus Decision
    # ----------------------------
    decision = consensus.get_decision(
        technical_signal="BUY",
        sentiment_signal="BUY",
        probability_score=92
    )

    print("\n========== FOREXMIND AI DAY 7 ==========\n")

    print(f"Decision      : {decision['decision']}")
    print(f"Confidence    : {decision['confidence']}%")
    print(f"Lot Size      : {lot}")
    print(f"Stop Loss     : {levels['stop_loss']}")
    print(f"Take Profit   : {levels['take_profit']}")

    # ----------------------------
    # Execute Trade
    # ----------------------------
    if decision["decision"] != "NO TRADE":

        trade = executor.open_trade(
            symbol="EURUSD",
            decision=decision["decision"],
            entry=1.17120,
            stop_loss=levels["stop_loss"],
            take_profit=levels["take_profit"],
            lot_size=lot
        )

        db.save_trade(trade)

        print("\n========== PAPER TRADE ==========\n")

        for key, value in trade.items():
            print(f"{key:<12}: {value}")

    else:
        print("\nNo trade executed.")

    # ----------------------------
    # Trade Journal
    # ----------------------------
    print("\n========== TRADE JOURNAL ==========\n")

    trades = db.get_all_trades()

    for record in trades:
        print(record)

    db.close()

    # ----------------------------
    # Performance Analytics
    # ----------------------------
    analytics = PerformanceAnalytics()

    stats = analytics.get_statistics()

    print("\n========== PERFORMANCE ==========\n")

    for key, value in stats.items():
        print(f"{key:<20}: {value}")

    analytics.close()


if __name__ == "__main__":
    main()