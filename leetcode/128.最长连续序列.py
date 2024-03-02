class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        st = set(nums)
        ans = 0
        for i in range(n):
            cur = nums[i]
            cnt = 1
            if nums[i]-1 in st: continue
            while cur + 1 in st:
                cur += 1
                cnt += 1
            ans = max(ans, cnt)
        return ans