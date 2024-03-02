class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂解法
        # 10 = 1010
        ans = 1
        sign = -1 if n < 0 else 1
        n = abs(n)
        while n:
            if n & 1:
                ans = ans * x
            x = x * x
            n >>= 1
        return 1 / ans if sign == -1 else ans