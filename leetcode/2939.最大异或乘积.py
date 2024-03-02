class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        x, y = a >> (n), b >> (n)
        x, y = x << (n), y << (n)
        for i in range(n-1, -1, -1):
            if (a>>i) & 1 == (b >> i) & 1:
                x, y = x | (1 << i), y | (1 << i)
            else:
                if x > y:
                    x, y = x, y|(1 << i)
                else:
                    x, y = x|(1 << i), y
        Mod = 10**9 + 7
        return ((x % Mod) * (y % Mod)) % Mod
            