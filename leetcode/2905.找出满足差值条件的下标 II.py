import sortedcontainers
from sortedcontainers import *
class Solution:
    def findIndices(self, nums: List[int], idf: int, vdf: int) -> List[int]:
        n = len(nums)
        st = SortedList()
        for i in range(n - idf):
            j = i + idf
            st.add((nums[i], i))
            if abs(st[0][0] - nums[j]) >= vdf:
                return [st[0][1], j]
            if abs(st[-1][0] - nums[j]) >= vdf:
                return [st[-1][1], j]
        return [-1, -1]