class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                t = nums[i] | nums[j]
                t = bin(t)
                if t[-1] == '0':
                    return True
        return False