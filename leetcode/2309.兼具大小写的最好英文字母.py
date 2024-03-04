class Solution:
    def greatestLetter(self, s: str) -> str:
        dic=Counter(s)
        ans=""
        for c in s:
            if c.islower() and chr(ord(c)-ord('a')+ord('A')) in dic:
                ans=max(c,ans)
        return ans.upper()