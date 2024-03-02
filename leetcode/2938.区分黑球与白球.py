class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        bai = 0
        ans = 0
        for i in range(n - 1, - 1, -1):
            if s[i] == '1':
                ans += bai
            else:
                bai += 1
        return ans