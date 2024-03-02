class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        up = int(sqrt(2 * n))
        cnt = 0
        for i in range(1, up + 1):
            if n % i == 0 and i % 2 == 1:
                cnt += 1
            if (n % i) * 2 == i:
                cnt += 1
        return cnt