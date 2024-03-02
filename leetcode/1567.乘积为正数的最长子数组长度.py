class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n + 1)]
        for i in range(1, n + 1):
            t = nums[i - 1] // abs(nums[i - 1]) if nums[i - 1] else 0
            if t == 0: continue
            if t == 1:
                f[i][1] = f[i - 1][1] + 1
                if f[i - 1][0]:
                    f[i][0] = f[i - 1][0] + 1
            if t < 0:
                f[i][0] = f[i - 1][1] + 1
                if f[i - 1][0]:
                    f[i][1] = f[i - 1][0] + 1
        return max(f[i][1] for i in range(n + 1))