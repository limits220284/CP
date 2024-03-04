class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ans=''
        alp=[None]*26
        t=0
        for i,c in enumerate(key):
            if c!=' ':
                if alp[ord(c)-ord('a')]==None:
                    alp[ord(c)-ord('a')]=chr(ord('a')+t)
                    t+=1
        for c in message:
            k=' ' if c==' ' else alp[ord(c)-ord('a')]
            ans+=k
        return ans