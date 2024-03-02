class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        return sum((pow(2, i, MOD) - pow(2, len(nums) - 1 - i, MOD)) * x
                   for i, x in enumerate(nums)) % MOD