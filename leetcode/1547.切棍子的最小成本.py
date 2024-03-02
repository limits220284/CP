class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        arr = []
        cuts = [0] + cuts + [n]
        for x, y in pairwise(cuts):
            arr.append(y - x)
        print(arr)
        m = len(arr)
        pre = [0]
        for x in arr: pre.append(pre[-1] + x)
        print(pre)
        # 区间dp
        # 定义f[i][j]表示合并i-j的最小花费
        # f[i]][j] = min(f[i][mid] + f[mid][j] + sum(arr[i:j+1]))
        # f[i][i] = arr[i]
        f = [[inf] * m for _ in range(m)]
        for i in range(m): f[i][i] = 0
        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):
                for mid in range(i, j):
                    f[i][j] = min(f[i][j], f[i][mid] + f[mid + 1][j] + pre[j + 1] - pre[i])
        return f[0][m - 1]