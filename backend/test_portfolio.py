from portfolio.portfolio_manager import portfolio_manager

trade = {
    "pair": "EUR/USD",
    "direction": "BUY",
    "lot": 0.10,
}

portfolio_manager.add_trade(trade)

portfolio_manager.close_trade(trade, 125.75)

print("=" * 60)
print(portfolio_manager.portfolio_summary())
print("=" * 60)