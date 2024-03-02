class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        tot = sum(cardPoints[n-k:])
        ans = tot
        for i in range(k):
            tot -= cardPoints[n-k+i]
            tot += cardPoints[i]
            ans = max(ans, tot)
        return ans