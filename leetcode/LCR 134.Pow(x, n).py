class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1 if n < 0 else 0
        ans = 1
        n = abs(n)
        while n:
            if n & 1:
                ans = ans * x
            n >>= 1
            x = x * x
        return 1/ans if sign else ans