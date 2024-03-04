class Solution:
    def minimumMoves(self, s: str) -> int:
        n=len(s)
        i=0
        ans=0
        while i<n:
            if s[i]=='X':
                ans+=1
                i+=2
            i+=1
        return ans   