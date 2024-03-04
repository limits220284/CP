class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.que=deque()
        self.sum=0
        self.mx=size

    def next(self, val: int) -> float:
        if len(self.que)==self.mx:
            self.sum-=self.que[0]
            self.que.popleft()
        self.sum+=val
        self.que.append(val)
        return self.sum/len(self.que)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)