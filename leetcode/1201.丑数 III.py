class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        L1 = a // gcd(a, b) * b
        L2 = a // gcd(a, c) * c
        L3 = c // gcd(b, c) * b
        LL = L1 // gcd(L1, c) * c
        l, r = 0, 100000000000000
        while l < r:
            mi = (l + r) // 2
            if mi // a + mi // b + mi // c - mi // L1 - mi // L2 - mi // L3 + mi // LL < n:
                l = mi + 1
            else:
                r = mi
        return l
