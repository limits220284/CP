class Solution:
    def reorderedPowerOf2(self, k: int) -> bool:
        dic=[[0 for i in range(10)] for j in range(30)]
        for i in range(30):
            n=2**i
            while n:
                dic[i][n%10]+=1
                n//=10
        ans=[0 for i in range(10)]
        while k:
            ans[k%10]+=1
            k//=10
        for i in range(30):
            flag=True
            for j in range(10):
                if ans[j]!=dic[i][j]:
                    flag=False
                    break
            if flag:
                return True
        return False
            