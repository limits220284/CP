#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
#

# @lc code=start
import sortedcontainers
from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        dic = defaultdict(int)
        pts = defaultdict(int)
        arr = SortedList()
        def find(x):
            if len(arr) == 0: return -1
            l, r = 0, len(arr)-1
            while l < r:
                mid = (l + r) // 2
                if arr[mid] > x:
                    r = mid
                else:
                    l = mid + 1
            if arr[l] < x:
                return -1
            idx = arr[l]
            arr.pop(l)
            return idx
        ans = [-1] * n
        for i, x in enumerate(rains):
            if x == 0:
                arr.add(i)
            else:
                if dic[x] == 0:
                    dic[x] = 1
                else:
                    k = find(pts[x])
                    if k == -1: return []
                    ans[k] = x
                pts[x] = i
        for x in arr:
            ans[x] = 1
        return ans
