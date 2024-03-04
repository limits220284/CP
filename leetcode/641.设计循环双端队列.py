class MyCircularDeque:

    def __init__(self, k: int):
        self.due=[0]*(k+1)
        self.head=0
        self.tail=0
        self.k=(k+1)
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head=(self.head-1)%self.k
        self.due[self.head]=value
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.due[self.tail]=value
        self.tail=(self.tail+1)%self.k
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head=(self.head+1)%self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail=(self.tail-1)%self.k
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.due[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.due[(self.tail-1)%self.k]

    def isEmpty(self) -> bool:
        if self.head==self.tail:
            return True
        return False

    def isFull(self) -> bool:
        if (self.tail+1)%self.k==self.head:
            return True
        return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()