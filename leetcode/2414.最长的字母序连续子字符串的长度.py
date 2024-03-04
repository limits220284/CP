class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        mx=1
        n=len(s)
        cnt=1
        for i in range(1,n):
            if ord(s[i])==ord(s[i-1])+1:
                cnt+=1
                mx=max(cnt,mx)
            else:
                cnt=1
        return mx
            