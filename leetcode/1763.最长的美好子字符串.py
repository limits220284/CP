class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n=len(s)
        res=0
        st=""
        for i in range(n):
            dp=[[False,False] for i in range(26)]
            if s[i]<='Z' and s[i]>='A':
                dp[ord(s[i])-ord('A')][0]=True
            else:
                dp[ord(s[i])-ord('a')][1]=True
            
            for j in range(i+1,n):
                if s[j]<='Z' and s[j]>='A':
                    dp[ord(s[j])-ord('A')][0]=True
                else:
                    dp[ord(s[j])-ord('a')][1]=True
                flag=True
                for x,y in dp:
                    if x!=y:
                       flag=False
                if flag:
                    if j-i+1>res:
                        st=s[i:j+1]
                        res=j-i+1
        return st