class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 只要互为质数即可
        return reduce(gcd, nums) == 1