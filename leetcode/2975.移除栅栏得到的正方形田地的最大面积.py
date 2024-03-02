class Solution:
    def maximizeSquareArea(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # 直接枚举左右两边，然后判断中间是否存在当前这种宽度的正方形即可
        h += [1, m]
        lh = len(h)
        h.sort()
        cnth = defaultdict()
        for i in range(lh):
            for j in range(i + 1, lh):
                cnth[h[j] - h[i]] = True
        v += [1, n]
        v.sort()
        # print(h, v, cnth)
        ans = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                if (v[j] - v[i]) in cnth:
                    ans = max(ans, (v[j] - v[i]) ** 2)
        if ans == -1:
            return ans
        return ans % MOD