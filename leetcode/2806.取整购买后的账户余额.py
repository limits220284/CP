class Solution:
    def accountBalanceAfterPurchase(self, p: int) -> int:
        if p % 10 == 5:
            return 100 - p - 5
        if p % 10 < 5:
            return 100 - (p - p % 10)
        return 100 - (p + 10 - p % 10)