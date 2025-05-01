class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        res = self.index - (-1 if not self.stack else self.stack[-1][1])
        self.stack.append((price, self.index))

        return res


# Your StockSpanner object will be instantiated and called as such:
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # return 1
print(stockSpanner.next(80))  # return 1
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(70))  # return 2
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(
    75))  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(stockSpanner.next(85))  # return 6
