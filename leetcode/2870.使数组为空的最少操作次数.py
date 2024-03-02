class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for v in cnt.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                ans += v // 3
            elif v % 3 == 1:
                ans += v // 3 + 1
            else:
                ans += v // 3 + 1
        return ans
            