class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        return (1 + n) * n // 2 - 2 * m * (1 + k) * k // 2