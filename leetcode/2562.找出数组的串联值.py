class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n-1
        ans = 0
        while i < j:
            ans += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        if i == j:
            ans += nums[i]
        return ans