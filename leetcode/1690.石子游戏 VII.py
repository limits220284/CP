class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        ## dp[i][j]表示最大得分差值
        pre = [0]
        for x in stones:
            pre.append(x + pre[-1])
        n = len(stones)
        # f[i][j] = max(sum(a[i+1:j]) - f[i+1:j], sum(a[i:j-1]) - f[i:j-1])
        f = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                f[i][j] = max(pre[j+1] - pre[i+1] - f[i+1][j], pre[j] - pre[i] - f[i][j-1])
        return f[0][n-1]
        
        