class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for x in range(min(n, limit) + 1):
            res = n - x
            if 2 * limit < res:
                continue
            ans += min(res, limit) - max(0, res - limit) + 1
        return ans