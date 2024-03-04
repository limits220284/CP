class MinStack:
    def __init__(self):
        self.s = []
        self.s_mn = []

    def push(self, x: int) -> None:
        self.s.append(x)
        if not self.s_mn:
            self.s_mn.append(x)
        else:
            y = self.s_mn[-1]
            self.s_mn.append(min(y,x))
        # print(self.s, self.s_mn)
    def pop(self) -> None:
        self.s.pop()
        self.s_mn.pop()


    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s_mn[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()