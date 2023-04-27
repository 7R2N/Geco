class TradePost:
    def __init__(self, reg):
        self.money = 0
        self.region = reg
        self.goods = None

    # method that provides transactions between TradePost and trader
    def trade(self):
        self.money += 5

    def refill(self):
        pass

    #TODO stan agenta