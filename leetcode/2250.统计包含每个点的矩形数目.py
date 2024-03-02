#
# @lc app=leetcode.cn id=2250 lang=python3
#
# [2250] 统计包含每个点的矩形数目
#

# @lc code=start
import sortedcontainers
from sortedcontainers import SortedList
class Solution:
    # 纵坐标排序
    def countRectangles_1(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 先将rectangles按着纵坐标进行排序
        n = len(points)
        rectangles.sort(key = lambda x: -x[1])
        # 然后将points按着纵坐标进行排序，如果当前纵坐标大于点的纵坐标，将横坐标加入到xs中
        # 对xs进行排序，然后二分查有多少个大于点横坐标的
        xs = []
        i = 0
        ans = [0] * n

        for point, idx in sorted(zip(points, range(n)), key = lambda x: -x[0][1]):
            xs_len = len(xs)
            while i < len(rectangles) and rectangles[i][1] >= point[1]:
                xs.append(rectangles[i][0])
                i += 1
            if len(xs) > xs_len: xs.sort()
            # 二分查找
            ans[idx] = len(xs) - bisect_left(xs, point[0])
        return ans
    # # 纵坐标排序 但是实时维护x的相对位置，采用SortedList
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 先将rectangles按着纵坐标进行排序
        n = len(points)
        rectangles.sort(key = lambda x: -x[1])
        # 然后将points按着纵坐标进行排序，如果当前纵坐标大于点的纵坐标，将横坐标加入到xs中
        # 对xs进行排序，然后二分查有多少个大于点横坐标的
        xs = SortedList()
        i = 0
        ans = [0] * n
        for point, idx in sorted(zip(points, range(n)), key = lambda x: -x[0][1]):
            while i < len(rectangles) and rectangles[i][1] >= point[1]:
                xs.add(rectangles[i][0])
                i += 1
            # 二分查找
            ans[idx] = len(xs) - bisect_left(xs, point[0])
        return ans
            
