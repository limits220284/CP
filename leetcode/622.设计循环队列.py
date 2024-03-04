class MyCircularQueue:
    def __init__(self, k: int):
        self.cque=[0 for i in range(k+1)]
        self.head=0
        self.tail=0
        self.k=k+1
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cque[self.tail]=value
        self.tail=(self.tail+1)%self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head=(self.head+1)%self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cque[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cque[(self.tail-1)%self.k]

    def isEmpty(self) -> bool:
        if self.tail==self.head:
            return True
        return False

    def isFull(self) -> bool:
        if (self.tail+1)%self.k==self.head:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()