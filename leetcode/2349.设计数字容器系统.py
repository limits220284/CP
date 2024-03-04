from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.m = {}
        self.ms = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.m:
            self.ms[self.m[index]].remove(index)  # 移除旧数据
        self.m[index] = number
        self.ms[number].add(index)  # 添加新数据

    def find(self, number: int) -> int:
        s = self.ms[number]
        return s[0] if s else -1