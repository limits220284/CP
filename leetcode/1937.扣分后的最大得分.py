"""
寻找重复子问题
f[i][j] 表示选中当前格子能够获得的最大分数
f[i][j] = max(f[i][j], f[i-1][k] - abs(k - j))
f[i][j] = max(f[i-1][0] - j, f[i-1][1] - j + 1, f[i-1][2]-j+2, ..., f[i-1][j], f[i-1][j+1]-1, .., f[i-1][n-1]-(n-1-j))
f[i][j+1] = max(f[i-1][0] - j - 1, f[i-1][1] - j, f[i-1][2]-j+1, ..., f[i-1][j] - 1, f[i-1][j+1], .., f[i-1][n-1]-(n-2-j))
f[i][j+1] = max(max(f[i-1][0] - j, f[i-1][1] - j + 1, f[i-1][2]-j+2, ..., f[i-1][j]) - 1, max(f[i-1][j+1]-1, .., f[i-1][n-1]-(n-1-j)) + 1)
"""
class Solution:
    def maxPoints1(self, f: List[List[int]]) -> int:
        m, n = len(f), len(f[0])
        for i in range(1, m):
            left, right = [0] * n, [0] * n
            mx = -inf
            for j in range(n - 1, -1, -1):
                mx = max(mx - 1, f[i-1][j])
                right[j] = mx
            mx = -inf
            for j in range(n):
                mx = max(mx - 1, f[i-1][j])
                left[j] = mx
            k = 0
            for j in range(n):
                f[i][j] += max(left[j], right[j])
                k += 1
        return max(f[-1])
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        f = deepcopy(points)
        for i in range(1, m):
            left, right = [0] * n, [0] * n
            mx = -inf
            for j in range(n):
                mx = max(f[i-1][j] + j, mx)
                left[j] = mx
            mx = -inf
            for j in range(n - 1, -1, -1):
                mx = max(f[i-1][j] - j, mx)
                right[j] = mx
            for j in range(n):
                f[i][j] = max(points[i][j] - j + left[j], points[i][j] + j + right[j])
        return max(f[-1])
                