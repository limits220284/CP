class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        f = 0
        for s in accumulate(satisfaction):
            f = max(f, f + s)
        return f
