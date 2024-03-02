"""
树形dp
f[i]表示当前点的满足条件的最长路径
1、如果左边的不等于自己，f[o] = f[o.left] + 1
2、如果右边的不等于自己，f[o] = f[o.right] + 1
3、如果左边和右边的都不等于自己 f[o] = f[o.left] + f[o.right] + 1
"""
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i, x in enumerate(parent):
            if i == 0: continue
            g[x].append(i)
            g[i].append(x)
        g[0].append(-1)
        print(g)
        ans = 1
        def dfs(x, fa):
            nonlocal ans
            if len(g[x]) == 1:
                return 1, s[x]
            res = []
            for y in g[x]:
                if y != fa:
                    res.append(dfs(y, x))
            # 将重复的去掉
            res = [t for t in res if t[1] != s[x]]
            if not res: return 1, s[x]
            ans = max(ans, res[0][0] + 1)
            if len(res) == 1: return res[0][0] + 1, s[x]
            res.sort(key = lambda x: x[0], reverse = True)
            ans = max(ans, res[0][0] + res[1][0] + 1)
            return res[0][0] + 1, s[x]
        dfs(0, -1)
        return ans