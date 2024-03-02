class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        def check(arr):
            for x, y in pairwise(arr):
                if x >= y:
                    return False
            return True
        ans = 0
        for i in range(n):
            for j in range(i, n):
                arr = nums[:i] + nums[j + 1:]
                if check(arr):
                    ans += 1
        return ans