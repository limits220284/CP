import sortedcontainers
from sortedcontainers import SortedList
class StockPrice:
    def __init__(self):
        self.cnt = Counter()
        self.st = SortedList()
        self.cur = -1
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.cnt:
            k = self.cnt[timestamp]
            self.st.remove(k)
        self.cnt[timestamp] = price
        self.st.add(price)
        self.cur = max(self.cur, timestamp)
    def current(self) -> int:
        return self.cnt[self.cur]

    def maximum(self) -> int:
        return self.st[-1]
    def minimum(self) -> int:
        return self.st[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()