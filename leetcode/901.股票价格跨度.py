class StockSpanner:

    def __init__(self):
        self.stack = []
        self.n = 0
    def next(self, price: int) -> int:
        self.n += 1
        ans = -1
        while len(self.stack) and self.stack[-1][0] <= price:
            self.stack.pop()
        if len(self.stack):
            ans = self.n - self.stack[-1][1]
        else:
            ans = self.n
        self.stack.append((price, self.n))
        return ans

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)