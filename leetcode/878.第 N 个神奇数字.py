class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lab = a * b // gcd(a, b)
        l, r = 0, int(1e18)
        while l < r:
            mid = (l + r) // 2
            if mid // a + mid // b - mid // lab < n:
                l = mid + 1
            else:
                r = mid
        return l % (10 ** 9 + 7)