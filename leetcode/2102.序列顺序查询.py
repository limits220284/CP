from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.st = SortedList()
        self.cnt = 0
    def add(self, name: str, score: int) -> None:
        self.st.add((-score, name))

    def get(self) -> str:
        self.cnt += 1
        return self.st[self.cnt - 1][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()