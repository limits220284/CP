class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr=encoding
        self.i=0
    def next(self, n: int) -> int:
        m=len(self.arr)
        while n:
            if self.i==m:
                return -1
            if self.arr[self.i]>=n:
                self.arr[self.i]-=n
                return self.arr[self.i+1]
            else:
                n-=self.arr[self.i]
                self.i+=2
        
                
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)