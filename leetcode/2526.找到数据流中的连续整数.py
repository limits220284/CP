class DataStream:

    def __init__(self, value: int, k: int):
        # 滑动窗口
        self.arr=[]
        self.dic=defaultdict(int)
        self.value=value
        self.k=k
        self.cnt=0

    def consec(self, num: int) -> bool:
        self.arr.append(num)
        self.cnt+=1
        self.dic[num]+=1
        if self.cnt<=self.k-1:
            return False
        if len(self.dic)==1 and self.dic[self.value]==self.k:
            self.dic[self.value]-=1
            return True
        pre=self.arr[-self.k]
        self.dic[pre]-=1
        if self.dic[pre]==0:
            del self.dic[pre]
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)