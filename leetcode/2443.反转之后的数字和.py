class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # 穷举大法
        if num==0:
            return True
        for x in range(num):
            t=x
            n=0
            while t:
                n=n*10+t%10
                t//=10
            if n+x==num:
                return True
        return False