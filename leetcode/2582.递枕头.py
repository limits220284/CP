class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k, t = divmod(time, n - 1)
        return n - t if k % 2 else 1 + t