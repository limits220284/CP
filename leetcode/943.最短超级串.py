class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlaps = [[0] * n for _ in range(n)]
        # 进行预处理
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if i == j: continue
                for ans in range(min(len(x), len(y)), -1, -1):
                    if x.endswith(y[:ans]):
                        overlaps[i][j] = ans
                        break
        # f[mask][i] 表示mask中以i元素结尾的重复的最多的
        f = [[0] * n for _ in range(1 << n)]
        parent = [[None] * n for _ in range(1 << n)]
        for mask in range(1, 1 << n):
            for i in range(n):
                if (mask >> i) & 1:
                    pmask = mask ^ (1 << i)
                    if pmask == 0: continue
                    for j in range(n):
                        if (pmask >> j) & 1:
                            value = f[pmask][j] + overlaps[j][i]
                            if value >= f[mask][i]:
                                f[mask][i] = value
                                parent[mask][i] = j # mask中以i结尾，前面一个元素是j

        # 通过记录的parent还原原来的结果
        perm = []
        mask = (1 << n) - 1
        i = max(range(n), key = f[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]
        perm = perm[::-1]
        # seen = [False] * n
        # for x in perm:
        #     seen[x] = True
        # perm.extend([i for i in range(n) if not seen[i]])
        ans = [words[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(words[perm[i]][overlap:])
        return "".join(ans)
        