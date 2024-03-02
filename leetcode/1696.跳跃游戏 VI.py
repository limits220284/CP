from sortedcontainers import SortedList
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # f[i] = max(f[i - 1] + nums[i], f[i - 2] + nums[i], ..., f[i - k] + nums[i])
        st = SortedList()
        f = [0] * n
        f[0] = nums[0]
        st.add(nums[0])
        for i in range(1, n):
            f[i] = st[-1] + nums[i]
            st.add(f[i])
            if i >= k:
                st.remove(f[i - k])
        return f[-1]
            