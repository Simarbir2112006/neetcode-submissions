class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        ticker = 1
        i = len(self.s) - 1
        while self.s and i >= 0 and self.s[i] <= price:
                ticker += 1
                i -= 1

        self.s.append(price)

        return ticker


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)