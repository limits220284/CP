#
# @lc app=leetcode.cn id=2392 lang=python3
#
# [2392] 给定条件下构造矩阵
#

# @lc code=start
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0] * k for _ in range(k)]
        def isvalid(arr):
            _IN = [0] * k
            g = [[] for _ in range(k)]
            for x, y in arr:
                x -= 1; y -= 1
                _IN[y] += 1
                g[x].append(y)
            q = deque(i for i, d in enumerate(_IN) if d == 0)
            ans = []
            while q:
                x = q.popleft()
                ans.append(x)
                for y in g[x]:
                    _IN[y] -= 1
                    if _IN[y] == 0:
                        q.append(y)
            if len(ans) == k:
                return ans
            return []
        row = isvalid(rowConditions)
        col = isvalid(colConditions)
        if not row or not col:
            return []
        pos = {x: i for i, x in enumerate(col)}
        for i in range(k):
            ans[i][pos[row[i]]] = row[i] + 1
        return ans
        

