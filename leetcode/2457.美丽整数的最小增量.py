class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # 突然有一个二分答案的想法,如果将n进行二分,因为答案具有最小值
        # 首先从小到大枚举target的值,然后判断从
        t=sum(int(i) for i in str(n))
        if t<=target:
            return 0
        n_s=str(n)
        m=len(n_s)
        
        s=['0']*(m+1)
        s[0]='1'
        s=int(''.join(s))
        r_s=str(s-n)
        # 穷举结果
        def check(y,x):
            y+=x
            y=str(y)
            tot=sum(int(i) for i in y)
            if tot<=target:
                return True
            return False
        for i in range(len(r_s)):
            x=int(r_s[-(i+1):])
            if check(n,x):
                return x
        return 0