class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        while True:
            x = 101
            for i in range(n):
                if nums[i]:
                    x = min(nums[i], x)
            if x == 101:
                break
            for i in range(n):
                if nums[i]:
                    nums[i] -= x
            ans += 1
        return ans