class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if i.bit_count() == k:
                ans += x
        return ans