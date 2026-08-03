import threading
import time

from market.live_market import update_prices
from market.market_cache import market_cache

thread = threading.Thread(
    target=update_prices,
    daemon=True,
)

thread.start()

while True:
    print("=" * 60)

    for symbol, data in market_cache.all().items():
        print(f"{symbol}")
        print(f"  Bid      : {data['bid']}")
        print(f"  Ask      : {data['ask']}")
        print(f"  Spread   : {data['spread']}")
        print(f"  Time     : {data['timestamp']}")
        print()

    time.sleep(2)