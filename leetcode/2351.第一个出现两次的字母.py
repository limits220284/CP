class Solution:
    def repeatedCharacter(self, s: str) -> str:
        tmp=0
        for c in s:
            x=ord(c)-ord('a')
            if tmp>>x&1:
                return c
            tmp|=1<<x