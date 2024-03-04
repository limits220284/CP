#采用sortedlist进行存储，设置s1,s2,s3
#先放数字用que存储，如果小于m，返回-1
#如果len(que)=m+1,需要删除最左边的数字
#  1、如果这个数字在s2中.直接删除即可
#  2、如果在s1中,s2最小的退下来一个
#  3、如果在s3中,s2最大的上去一个
import sortedcontainers
from sortedcontainers import SortedList
class MKAverage:
    def __init__(self, m: int, k: int):
        self.q=deque()
        self.s1=SortedList()
        self.s2=SortedList()
        self.s3=SortedList()
        self.m=m
        self.k=k
        self.sum2=0
    def addElement(self, num: int) -> None:
        if len(self.q)<self.m:
            self.q.append(num)
            if len(self.q)==self.m:
                a=list(self.q)
                a.sort()
                self.s1.update(a[:self.k])
                self.s2.update(a[self.k:-self.k])
                self.s3.update(a[-self.k:])
                self.sum2=sum(a[self.k:-self.k])
            return
        #加入新的元素
        self.q.append(num)
        if num<self.s1[-1]:
            self.s1.add(num)
            t=self.s1.pop()
            self.s2.add(t)
            self.sum2+=t
        elif num>self.s3[0]:
            self.s3.add(num)
            t=self.s3.pop(0)
            self.s2.add(t)
            self.sum2+=t
        else:
            self.s2.add(num)
            self.sum2+=num
        #删除左边元素
        t=self.q.popleft()
        if t in self.s2:
            self.s2.pop(self.s2.index(t))
            self.sum2-=t
        elif t in self.s1:
            self.s1.pop(self.s1.index(t))
            self.s1.add(self.s2[0])
            self.sum2-=self.s2.pop(0)
        elif t in self.s3:
            self.s3.pop(self.s3.index(t))
            self.s3.add(self.s2[-1])
            self.sum2-=self.s2.pop(-1)
        # print(self.s1,self.s2,self.s3)
        # print(self.sum2)
    def calculateMKAverage(self) -> int:
        if len(self.q)<self.m:
            return -1
        return self.sum2//(self.m-2*self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()