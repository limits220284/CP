#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#

# @lc code=start
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        s = sum(arr)
        if s == 0: return [0, 2]
        if s % 3 != 0: return [-1, -1]
        part = s // 3
        # 确定位置
        a, b, c = 0, 0, 0
        cur = 0
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    a = i
                elif cur == part:
                    b = i
                elif cur == 2 * part:
                    c = i
                cur += 1
        # 判断三段是否相同
        i = 0
        while i + c < n:
            if arr[a + i] != arr[c + i] or arr[b + i] != arr[c + i]:
                return [-1, -1]
            i += 1
        t = n - c
        return [a + t - 1, b + t]


