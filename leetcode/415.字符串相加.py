#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings1(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        flag, i, j = 0, 0, 0
        ans = ""
        while i < m and j < n:
            cur = (int(num1[i]) + int(num2[j]) + flag) % 10
            flag = (int(num1[i]) + int(num2[j]) + flag) // 10
            ans += str(cur)
            i += 1
            j += 1
        while i < m:
            cur = (int(num1[i]) + flag) % 10
            flag = (int(num1[i]) + flag) // 10
            ans += str(cur)
            i += 1
        while j < n:
            cur = (int(num2[j]) + flag) % 10
            flag = (int(num2[j]) + flag) // 10
            ans += str(cur)
            j += 1
        if flag:
            ans += "1"
        ans = ans[::-1]
        return ans
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        flag = 0
        ans = ""
        while i >= 0 or j >= 0 or flag != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            cur = x + y + flag
            ans += str(cur % 10)
            flag = cur // 10
            i -= 1
            j -= 1
        ans = ans[::-1]
        return ans
