class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        p = 0
        n = len(nums)
        for num in nums:
            p ^= num
        if p == k:
            return 0
        p = p ^ k
        ct = 0
        while p > 0:
            ct += p & 1
            p >>= 1
        return ct