class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans=0
        cnt=0
        for c in s:
            if int(c)>k:
                return -1
            t=cnt*10+int(c)
            if t<=k:
                cnt=t
            else:
                ans+=1
                cnt=int(c)
        return ans+1
                