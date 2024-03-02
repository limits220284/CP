class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        all = sum(nums)
        if all % k:
            return False
        per = all // k
        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)
        dp = [-1] * (1 << n)
        dp[0] = 0
        # 查表法,主要是判断当前该集合是否能够由先前的集合推理过来
        for i in range(0, 1 << n):
            for j in range(n):
                if i >> j & 1 == 0: continue
                s1 = i & ~(1 << j)
                if dp[s1] >= 0 and dp[s1] + nums[j] <= per:
                    dp[i] = (dp[s1] + nums[j]) % per
        return dp[(1 << n) - 1] == 0