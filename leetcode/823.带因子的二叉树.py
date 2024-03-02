class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        f = {}
        for x in arr: f[x] = 1
        for i, val in enumerate(arr):
            for j in range(i):  # val 的因子一定比 val 小
                x = arr[j]
                if x ** 2 > val: break
                if x ** 2 == val:
                    f[val] += f[x] ** 2
                    break
                if val % x == 0 and val // x in f:
                    f[val] += f[x] * f[val // x] * 2
        ans = 0
        for v in f.values():
            ans += v
        return ans % (10 ** 9 + 7)