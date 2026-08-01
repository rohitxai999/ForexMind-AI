import random
import time

from market.market_cache import market_cache

pairs = {
    "EURUSD": 1.1700,
    "GBPUSD": 1.3550,
    "USDJPY": 149.80,
    "AUDUSD": 0.6650,
    "USDCAD": 1.3720,
}


def update_prices():
    while True:
        for symbol, price in pairs.items():
            movement = random.uniform(-0.0005, 0.0005)

            bid = round(price + movement, 5)
            ask = round(bid + 0.0002, 5)

            market_cache.update(symbol, bid, ask)

        time.sleep(2)


if __name__ == "__main__":
    update_prices()