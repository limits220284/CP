class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans=[int(x) for x in str(n)]
        cnt=0
        for i,x in enumerate(ans):
            if i%2==0:
                cnt+=x
            else:
                cnt-=x
        return cnt