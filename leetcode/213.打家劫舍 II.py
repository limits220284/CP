class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def work(arr):
            m = len(arr)
            f = [0] * (m+1)
            f[1] = arr[0]
            for i in range(2, m+1):
                f[i] = max(f[i-1], f[i-2] + arr[i-1])
            return f[m]
        t1 = work(nums[1:])
        t2 = work(nums[:-1])
        return max(t1, t2)