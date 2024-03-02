class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = min(cnt.values())
        for k in range(mx, 0, -1):
            ans = 0
            for c in cnt.values():
                q, r = divmod(c, k)
                if q < r:
                    break
                ans += (c + k) // (k + 1)
            else:
                return ans
            