class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(target)
        g = [[inf] * 26 for _ in range(26)]
        m = len(original)
        for i in range(m):
            a, b = ord(original[i]) - ord('a'), ord(changed[i]) - ord('a')
            g[a][b] = min(g[a][b], cost[i])
        for i in range(26): g[i][i] = 0
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        ans = 0
        for i in range(n):
            a, b = ord(source[i]) - ord('a'), ord(target[i]) - ord('a')
            if g[a][b] == inf:
                return -1
            ans += g[a][b]
        return ans