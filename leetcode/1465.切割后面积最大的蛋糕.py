class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        a, b = max(horizontalCuts[0], h - horizontalCuts[-1]), max(verticalCuts[0], w - verticalCuts[-1])
        for x, y in pairwise(horizontalCuts):
            a = max(a, y - x)
        for x, y in pairwise(verticalCuts):
            b = max(b, y - x)
        return a * b % (10 ** 9 + 7)