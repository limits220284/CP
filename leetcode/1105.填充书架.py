class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # 动态规划解法
        # 当前书是选择放在和上一本书同一层，还是新开一层
        # 记忆化搜索来解决当前问题
        # dfs(i) 表示前i本书构成的最小高度
        # 分组dp
        # f[i] = min(f[i-1] + books[i][1], f[i-2] + books[i][1] + books[i-1][1], f[i-3] + books[i-2-][1])
        # 需要求一下前缀和
        n = len(books)
        f = [inf] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            # 前缀和优化，优化最大值
            s, mx = 0, 0
            for j in range(i, 0, -1):
                s += books[j-1][0]
                mx = max(mx, books[j-1][1])
                if s <= shelfWidth:
                    f[i] = min(f[i], f[j-1] + mx)
                else:
                    break
        print(f)
        return f[n]