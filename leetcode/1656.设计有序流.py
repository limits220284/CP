class OrderedStream:

    def __init__(self, n: int):
        self.s=['']*(n+1)
        self.ptr=1
        self.n=n+1
    def insert(self, idKey: int, value: str) -> List[str]:
        if idKey!=self.ptr:
            self.s[idKey]=value
        self.s[idKey]=value
        res=[]
        while self.ptr<self.n and self.s[self.ptr]!='':
            res.append(self.s[self.ptr])
            self.ptr+=1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)