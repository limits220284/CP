class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        m = (n+1) // 2
        j = m
        cnt = 0
        i = 0
        while i < m:
            while j < n:
                if nums[i] < nums[j]:
                    i += 1
                    j += 1
                    cnt += 2
                elif nums[i] == nums[j]:
                    j += 1
            i += 1
        return n - cnt
        
                    
                    
        