import collections
from collections import defaultdict
import bisect
from bisect import *
#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        fx = 0
        x, y = 0, 0
        h = defaultdict(list)
        v = defaultdict(list)
        for i, j in obstacles:
            h[j].append(i)
            v[i].append(j)
        for i in h: h[i].sort()
        for i in v: v[i].sort()
        ans = 0
        for c in commands:
            if c >= 0:
                x2, y2 = 0, 0
                d = 1 - fx // 2 * 2  # 1 代表正方向，-1代表负的方向
                if fx % 2 == 0: # 上下
                    y2 = y + d * c
                    arr = v[x]
                    if d == 1:
                        idx = bisect_right(arr, y) #返回第一个大于x的下标，如果数组为空，返回0，如果全都小于x，则返回
                        # 如果下标在范围内，并且找到的
                        if idx < len(arr) and y2 >= arr[idx]:
                            y2 = arr[idx] - 1
                    else:
                        idx = bisect_left(arr, y) - 1
                        if idx >= 0 and y2 <= arr[idx]:
                            y2 = arr[idx] + 1
                    y = y2
                else: # 左右
                    x2 = x + d * c
                    arr = h[y]
                    if d == 1:
                        idx = bisect_right(arr, x) #返回第一个大于x的下标，如果数组为空，返回0，如果全都小于x，则返回n
                        if idx < len(arr) and x2 >= arr[idx]:
                            x2 = arr[idx] - 1
                    else:
                        idx = bisect_left(arr, x) - 1
                        if idx >= 0 and x2 <= arr[idx]:
                            x2 = arr[idx] + 1
                    x = x2
                ans = max(ans, x ** 2 + y ** 2)
            elif c == -2:
                fx = (fx - 1) % 4
            else:
                fx = (fx + 1) % 4
        return ans