class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ans = []
        IN = [0] * n
        for x, y in edges:
            IN[y] += 1
        for i in range(n):
            if IN[i] == 0:
                ans.append(i)
        if len(ans) >= 2:
            return -1
        return ans[0]