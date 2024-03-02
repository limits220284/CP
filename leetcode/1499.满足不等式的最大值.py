import sortedcontainers
from sortedcontainers import SortedList
class Solution:
    def findMaxValueOfEquation1(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        q = SortedList()
        ans = -inf
        l = 0
        for i in range(n-1):
            q.add((points[i][1] - points[i][0], points[i][0]))
            while q and points[i+1][0] - points[l][0] > k:
                q.remove((points[l][1] - points[l][0], points[l][0]))
                l += 1
            if q: ans = max(ans, sum(points[i+1]) + q[-1][0])
        return ans
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # 单调队列模版题目
        q = deque()
        ans = -inf
        for x, y in points:
            while q and q[0][0] < x - k:
                q.popleft()
            if q: ans = max(ans, x + y + q[0][1])
            while q and q[-1][1] <= y - x:
                q.pop()
            q.append((x, y - x))
        return ans

            