MX = 1000
primes = [0]
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pre = 0
        for x in nums:
            if x <= pre:
                return False
            j = bisect_left(primes, x - pre) - 1
            pre = x - primes[j]
        return True