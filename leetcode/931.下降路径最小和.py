class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [[inf] * (n+2) for _ in range(n)]
        for i in range(1, n+1): f[0][i] = matrix[0][i-1]
        for i in range(1, n):
            for j in range(1, n+1):
                f[i][j] = min(f[i-1][j-1], f[i-1][j], f[i-1][j+1]) + matrix[i][j-1]
        return min(f[-1])