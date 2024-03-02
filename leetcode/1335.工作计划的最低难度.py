class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # f = [[inf] * (d + 1) for _ in range(n+1)]
        # if n < d:return -1
        # f[0][0] = 0
        # for i in range(1, n+1):
        #     for j in range(1, d+1):
        #         if i < j:continue
        #         mx = 0
        #         for k in range(i-1, j-2, -1):
        #             mx = max(jobDifficulty[k], mx)
        #             f[i][j] = min(f[i][j], f[k][j-1] + mx)
        # # print(f) 
        # return f[n][d]
        if n < d:return -1
        dic = {}
        def dfs(i, j):
            if (i, j) in dic:
                return dic[(i, j)]
            res, mx = inf, 0
            if j == 0:
                dic[(i, j)] = max(jobDifficulty[:i+1])
                return max(jobDifficulty[:i+1])
            for k in range(i-1, j-2, -1):
                mx = max(jobDifficulty[k+1], mx)
                res = min(res, mx + dfs(k, j-1))
            dic[(i, j)] = res
            return res
        return dfs(n-1, d-1)
