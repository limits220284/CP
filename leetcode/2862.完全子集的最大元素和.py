@cache
def core(n):
        res = 1
        for i in range(2, isqrt(n) + 1):
            e = 0
            if n % i == 0:
                while n % i == 0:
                    n //= i
                    e += 1
            if e % 2:
                res *= i
        if n > 1:
            res *= n
        return res

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n+1)
        for i in range(1, n + 1):
            s[core(i)] += nums[i-1]
        return max(s)