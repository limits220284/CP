class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid: row.sort(reverse = True)
        ans = 0
        for row in zip(*grid):
            ans += max(row)
        return ans