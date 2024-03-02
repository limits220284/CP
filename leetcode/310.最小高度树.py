class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        height0 = [0] * n
        # 计算以当前为根节点，子树的高度
        def dfs(x, fa):
            height0[x] = 1
            h = 0
            for y in g[x]:
                if y != fa:
                    dfs(y, x)
                    h = max(h, height0[y])
            height0[x] = h + 1
        dfs(0, -1)
        height = [0] * n
        def reroot(x, fa):
            first, second = 0, 0
            for y in g[x]:
                if height0[y] > first:
                    second = first
                    first = height0[y]
                elif height0[y] > second:
                    second = height0[y]
            for y in g[x]:
                if height[y] != 0: continue
                height0[x] = (first if height0[y] != first else second) + 1 
                height[y] = max(height0[y], height0[x] + 1)
                reroot(y, x)
        reroot(0, -1)
        ans = []
        h = n
        for i in range(n):
            if height[i] < h:
                h = height[i]
                ans = []
            if height[i] == h:
                ans.append(i)
        return ans