import sortedcontainers
from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        st = SortedList()
        ans = inf
        for i in range(k, n):
            x = nums[i]
            st.add(nums[left])
            l, r = 0, len(st)-1
            while l < r:
                mid = (l + r) // 2
                if st[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            if l != 0: ans = min(ans, abs(st[l-1] - x))
            ans = min(ans, abs(st[l] - x))
            left += 1
        return ans
            