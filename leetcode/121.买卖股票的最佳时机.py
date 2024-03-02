class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        ans = 0
        for x in reversed(prices):
            mx = max(mx, x)
            ans = max(ans, mx - x)
        return ans