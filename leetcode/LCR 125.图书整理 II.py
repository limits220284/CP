class CQueue:

    def __init__(self):
        self.stk1=[]
        self.stk2=[]

    def appendTail(self, value: int) -> None:
        self.stk1.append(value)

    def deleteHead(self) -> int:
        if self.stk2:return self.stk2.pop()
        if not self.stk1:return -1
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        return self.stk2.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()