class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # 动态规划,二维线性dp
        # dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]),要么从左边下来,要么从上面下来
        # 方案数也是一样
        MIN = -float('inf')
        MOD = 10**9 + 7
        m, n = len(board), len(board[0])
        dp = [[0] * n for _ in range(m)]
        g = [[0] * n for _ in range(m)]
        g[0][0] = 1
        for i in range(m):
            cnt = [[MIN,0] for i in range(3)] #代表方案数,前面是最大得分,后面是最大得分的方案数
            mx = 0
            for j in range(n):
                if i == 0 and j == 0:continue
                if board[i][j] == 'X':
                    t = MIN
                elif board[i][j] == 'E' or board[i][j] == 'S':
                    t = 0
                else:
                    t = int(board[i][j])
                if i > 0:
                    cnt[0][0] = dp[i-1][j] + t
                    cnt[0][1] = g[i-1][j]
                if j > 0:
                    cnt[1][0] = dp[i][j-1] + t
                    cnt[1][1] = g[i][j-1]
                if i > 0 and j > 0:
                    cnt[2][0] = dp[i-1][j-1] + t
                    cnt[2][1] = g[i-1][j-1]
                mx = max(cnt[i][0] for i in range(3))
                dp[i][j] = mx
                g[i][j] = sum(cnt[i][1] if cnt[i][0] == mx else 0 for i in range(3)) % MOD
        if dp[m-1][n-1] < 0:
            return [0,0]
        return [dp[m-1][n-1],g[m-1][n-1]]