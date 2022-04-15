class StockTickerDailyResult:
    def __init__(self,
                 close_price,
                 open_price,
                 max_price,
                 min_price,
                 volume,
                 transactions,
                 timestamp,
                 volume_weighted_average_price):
        self.v = volume
        self.vw = volume_weighted_average_price
        self.o = open_price
        self.c = close_price
        self.h = max_price
        self.l = min_price
        self.t = timestamp
        self.n = transactions
