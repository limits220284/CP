class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        ans = 0
        for i in range(n):
            st = set()
            for j in range(i, n):
                st.add(nums[j])
                ans = (ans + len(st) ** 2) % MOD
        return ans