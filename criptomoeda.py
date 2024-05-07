class Criptomoeda:
    def __init__(self, symbol: str, lastPrice: float, nextFundingTime: str):
        self.symbol = symbol
        self.lastPrice = lastPrice
        self.nextFundingTime = nextFundingTime

    def __str__(self):
        if len(self.symbol) > 3:
            symbol_display = self.symbol[:3] + "..."
        else:
            symbol_display = self.symbol
        return f"symbol: {symbol_display}, lastPrice: {self.lastPrice}, nextFundingTime: {self.nextFundingTime}"
