from portfolio.trade_lifecycle import trade_lifecycle

trade = trade_lifecycle.create_trade(
    pair="EUR/USD",
    direction="BUY",
    entry_price=1.1700,
)

trade_lifecycle.activate_trade(trade)

trade_lifecycle.close_trade(
    trade,
    exit_price=1.1745,
    profit=45.20,
)

print("=" * 60)

for t in trade_lifecycle.get_all():
    print(t)

print("=" * 60)