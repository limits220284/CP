class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # 经典滑动窗口
        m = len(set(nums))
        n = len(nums)
        l, r = 0, 0
        st = Counter()
        ans = 0
        while r < n:
            st[nums[r]] += 1
            while len(st) == m:
                st[nums[l]] -= 1
                if st[nums[l]] == 0:
                    del st[nums[l]]
                l += 1
                ans += n - r
            r += 1
        return ans