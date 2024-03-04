class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt=0
        ans=0
        for c in s:
            if c=='|':
                cnt=(cnt+1)%2
            elif c=='*':
                if cnt==0:
                    ans+=1
        return ans
            