class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        g = [[] for _ in range(n)]
        for x, fa in enumerate(parents):
            if fa == -1:continue
            g[fa].append(x)
        dis = [[] for _ in range(n)]
        def dfs(x, fa):
            # 返回的是以x为根的子树大小
            cnt = 1
            for y in g[x]:
                if y != fa:
                    k = dfs(y, x)
                    dis[x].append(k)
                    cnt += k
            return cnt
        dfs(0, -1)
        ans = []
        # print(g)
        # print(dis)
        for arr in dis:
            m = len(arr)
            cnt = 1
            tot = 0
            if m == 2:
                cnt = arr[0] * arr[1]
            elif m == 1:
                cnt = arr[0]
            else:
                cnt = n - 1
            r = n - 1 - sum(arr) 
            cnt *= 1 if not r or r == n - 1 else r
            ans.append(cnt)
        mx = max(ans)
        # print(ans)
        return sum(1 if x == mx else 0 for x in ans)
        