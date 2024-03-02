class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        q = []
        ans = []
        for x in obstacles:
            l, r = 0, len(q) - 1
            while l < r:
                mid = (l + r) // 2
                if q[mid] > x:
                    r = mid
                else:
                    l = mid + 1
            if not q or q[l] <= x:
                q.append(x)
                l = len(q)
            else:
                q[l] = x
                l += 1
            ans.append(l)
        return ans
