class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        arr = []
        for i, x in enumerate(seats):
            if x == 1: arr.append(i)
        ans = max(arr[0], len(seats) - arr[-1] - 1)
        for x, y in pairwise(arr):
            ans = max(ans, (y - x) // 2)
        return ans