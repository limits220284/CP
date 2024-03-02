#
# @lc app=leetcode.cn id=880 lang=python3
#
# [880] 索引处的解码字符串
#

# @lc code=start
class Solution:
    def decodeAtIndex1(self, s: str, k: int) -> str:
        f = [(0, 1, 0, "")]
        cnt = 0
        word = ""
        for i, c in enumerate(s):
            if c.isalpha():
                cnt += 1
                word += c
            else:
                f.append(((cnt + f[-1][0]) * int(s[i]), int(s[i]), cnt, word))
                cnt = 0
                word = ""
        l, r = 0, len(f) - 1
        while l < r:
            mid = (l + r) // 2
            if f[mid][0] >= k:
                r = mid
            else:
                l = mid + 1
        if f[l][0] < k:
            return word[k - f[l][0] - 1]
        while True:
            block = f[l][0] // f[l][1]
            d = k
            if k > block:
                d = k % block
                if d == 0:
                    d = block
            pre = block - f[l][2]
            if d > pre:
                return f[l][3][d - pre - 1]
            else:
                l -= 1
                k = d
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                size //= int(c)
            else:
                size -= 1

