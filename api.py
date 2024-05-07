import requests
from typing import List
from criptomoeda import Criptomoeda


def get_data() -> List[Criptomoeda]:
    response = requests.get(
        "https://api-testnet.bybit.com/v5/market/tickers?category=inverse"
    )
    data = response.json()
    criptomoedas = [
        Criptomoeda(
            item["symbol"][:3] + "..." if len(item["symbol"]) > 3 else item["symbol"],
            float(item["lastPrice"]),
            item["nextFundingTime"],
        )
        for item in data["result"]["list"]
    ]
    criptomoedas.sort(key=lambda x: x.lastPrice, reverse=True)
    return criptomoedas[:5]
