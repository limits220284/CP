from sortedcontainers import SortedDict
class MyCalendarTwo:
    #差分数组解法
    def __init__(self):
        self.cnt=SortedDict()
    def book(self, start: int, end: int) -> bool:
        self.cnt[start]=self.cnt.get(start,0)+1
        self.cnt[end]=self.cnt.get(end,0)-1
        mx=0
        for c in self.cnt.values():
            mx+=c
            if mx>2:
                self.cnt[start]=self.cnt.get(start,0)-1
                self.cnt[end]=self.cnt.get(end,0)+1
                return False
        return True        
            


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)