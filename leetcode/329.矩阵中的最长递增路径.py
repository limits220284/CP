class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 记忆化搜索
        # dfs(i, j)表示(i, j)点为结尾的最长递增路径的长度
        ans = 0
        m, n = len(matrix), len(matrix[0])
        inx = [0, 0, -1, 1]
        iny = [1, -1, 0, 0]
        @cache
        def dfs(i ,j):
            res = 0
            for k in range(4):
                dx, dy = i + inx[k], j + iny[k]
                if 0 <= dx < m and 0 <= dy < n and matrix[dx][dy] < matrix[i][j]:
                    res = max(res, dfs(dx, dy))
            return res + 1
            
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans