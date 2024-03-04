class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #动态规划解法
        n,m=len(s),len(t)
        dp=[[m for _ in range(26)] for i in range(m+1)]
        #初始化dp数组
        for i in range(m-1,-1,-1):
            for j in range(26):
                if ord(t[i])-ord('a')==j:
                    dp[i][j]=i
                else:
                    dp[i][j]=dp[i+1][j]
        #进行寻找
        start=0
        for i in range(n):
            if dp[start][ord(s[i])-ord('a')]==m:
                return False
            start=dp[start][ord(s[i])-ord('a')]+1
        return True
            