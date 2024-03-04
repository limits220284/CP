class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        #归并是可以做的
        n=len(nums)
        while n!=1:
            for i in range(n//2):
                if i%2:
                    nums[i]=max(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i]=min(nums[2 * i], nums[2 * i + 1])
            n//=2
        return nums[0]