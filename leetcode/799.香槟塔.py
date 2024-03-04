class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0] * 100
        dp[0] = poured
        for i in range(query_row):
            for j in range(min(i, query_glass), -1, -1):
                tmp = dp[j]
                dp[j] = 0
                if tmp > 1:
                    dp[j+1] += (tmp-1)/2
                    dp[j] += (tmp-1)/2
        return min(1, dp[query_glass])
