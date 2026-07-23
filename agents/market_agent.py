from services.forex_api import get_forex_data

class MarketAgent:

    def __init__(self):
        self.symbols = [
            "EURUSD=X",
            "GBPUSD=X",
            "USDJPY=X",
            "AUDUSD=X",
            "USDCAD=X",
            "USDCHF=X",
            "NZDUSD=X"
        ]

    def collect_market(self):
        market = {}

        for symbol in self.symbols:
            market[symbol] = get_forex_data(symbol)

        return market