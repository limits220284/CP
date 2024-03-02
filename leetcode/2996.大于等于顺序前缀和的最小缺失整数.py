class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        mxn = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                mxn+=nums[i]
            else:
                break
            
        while mxn in s:
            mxn+=1
        return mxn