class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # 统计不同组的数量n,然后计算2**n即可
        ranges.sort()
        merge = []
        for i, [l, r] in enumerate(ranges):
            if not merge or merge[-1][1] < l:
                merge.append([l, r])
            if merge[-1][1] >= l:
                merge[-1][1] = max(merge[-1][1], r)
        MOD = 10**9 + 7
        # 快速幂
        def qmi(a, k, p):
            res = 1
            while k:
                if k & 1:
                    res = (res * a) % p
                a = (a * a) % p
                k >>= 1
            return res
        return qmi(2, len(merge), MOD)
        