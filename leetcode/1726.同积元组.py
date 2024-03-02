class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                cnt[nums[i] * nums[j]] += 1
        ans = 0
        for k, v in cnt.items():
            ans += v * (v - 1) * 4
        return ans 
