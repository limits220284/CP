class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # 枚举最小值,然后累加最大值
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        pre = 0
        n = len(nums)
        for i in range(n-1, -1, -1):
            ans = (ans + nums[i] ** 3 + nums[i] * pre)%MOD
            pre = (pre * 2 + nums[i] ** 2) % MOD
        return ans