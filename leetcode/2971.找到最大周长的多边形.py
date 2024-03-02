class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        n = len(nums)
        pre = nums[0] + nums[1]
        ans = 2
        for i in range(2, n):
            if nums[i] < pre:
                ans = max(ans, i + 1)
            pre += nums[i]
        if ans == 2:
            return -1
        return sum(nums[:ans])
            
            
            