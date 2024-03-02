class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        for c in str(num):
            if num % int(c) == 0:
                ans += 1
        return ans