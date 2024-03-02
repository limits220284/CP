#
# @lc app=leetcode.cn id=1625 lang=python3
#
# [1625] 执行操作后字典序最小的字符串
#

# @lc code=start
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        ans = s
        s = list(s)
        k_limit = 0 if b % 2 == 0 else 9
        for i in range(0, n, gcd(n,b)):
            for j in range(10):
                for k in range(k_limit+1):
                    ss = s[-i:] + s[:-i]
                    for p in range(0, n, 2):
                        ss[p] = str((int(ss[p]) + a * k) % 10)
                    for p in range(1, n, 2):
                        ss[p] = str((int(ss[p]) + a * j) % 10)
                    ans = min(ans, "".join(ss))
        return ans