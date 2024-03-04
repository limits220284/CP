class Solution:
    def maxScore(self, s: str) -> int:
        n_1=sum(int(x) for x in s)
        n=len(s)
        res=0
        cnt=0
        for i in range(n-1):
            if s[i]=='1':
                cnt+=1
            res=max(res,i+1-cnt+n_1-cnt)
        return res