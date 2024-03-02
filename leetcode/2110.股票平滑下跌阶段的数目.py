class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        i, n = 0, len(prices)
        ans = 0
        while i < n:
            start = i
            while i < n-1 and prices[i] - prices[i+1] == 1:
                i += 1
            ans += (i - start + 1) * (i - start + 2) // 2
            i += 1
        return ans