class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        mi = inf
        ans = 0
        for p in prices:
            ans = max(ans, p - mi)
            mi = min(mi, p)
        return ans