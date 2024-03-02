class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i, n = 0, len(nums)
        while i < n:
            start = i
            while i < n-1 and nums[i]+1 == nums[i+1]:
                i += 1
            s = str(nums[start])
            if start < i:
                s += '->' + str(nums[i])
            ans.append(s)
            i += 1
        return ans