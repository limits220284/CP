class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def work(x):
            if x < 2:
                return False
            for i in range(2, int(sqrt(x))+1):
                if x % i == 0:
                    return False
            return True
        n = len(nums)
        ans = 0;
        for i in range(n):
            if work(nums[i][i]):
                ans = max(ans, nums[i][i])
            if work(nums[i][n - i - 1]):
                ans = max(ans, nums[i][n - i - 1])
        return ans
                