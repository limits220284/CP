class Solution:
    def countTestedDevices(self, bp: List[int]) -> int:
        ans = 0
        n = len(bp)
        cnt = 0
        for i in range(n):
            if bp[i] - cnt > 0:
                cnt += 1
                ans += 1
        return ans