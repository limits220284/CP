"""
动态规划解法，无后效性
考虑一个长方体，最长的一条边当高即可
考虑两个长方体，有一个在底部，
"""
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort()
        f = [0] * len(cuboids)
        for i, (_, l2, h2) in enumerate(cuboids):
            f[i] = h2
            for j, (_, l1, h1) in enumerate(cuboids[:i]):
                if l1 <= l2 and h1 <= h2:
                    f[i] = max(f[i], f[j] + h2)
        return max(f)