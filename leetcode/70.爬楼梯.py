class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:return n
        a, b = 1, 2
        for i in range(2, n):
            t = a + b
            a, b = b, t
        return b
        