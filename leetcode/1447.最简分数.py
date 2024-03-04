class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # 暴力求解
        def gcd(x,y):
            return x if y==0 else gcd(y,x%y)
        ans=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if gcd(i,j)==1:
                    ans.append(str(j)+'/'+str(i))
        return ans