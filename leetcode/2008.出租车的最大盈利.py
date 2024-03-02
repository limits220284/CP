"""
f[i] 表示最后距离所能获得的最大利润
"""
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        f = [0] * (n + 1)
        rides.sort(key = lambda x: x[1])
        hsh = defaultdict(list)
        for start, end, tip in rides:
            hsh[end].append([start, tip])
        for i in range(1, n + 1):
            f[i] = max(f[i], f[i - 1])
            for t in hsh[i]:
                start, tip = t
                f[i] = max(f[i], f[start] + tip + i - start)
        return f[-1]
        # for start, end, tip in rides:
        #     f[end] = max(f[end], f[end - 1])
        #     f[end] = max(f[end], f[start] + tip + end - start)
        # print(f)
        # return max(f)