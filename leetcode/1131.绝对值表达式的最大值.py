class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        ans = 0
        # 枚举四个方向
        for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            maxv = -inf
            minv = inf
            # 计算当前方向上的曼哈顿距离最小值和最大值
            for i in range(n):
                maxv = max(maxv, arr1[i] * dx + arr2[i] * dy + i)
                minv = min(minv, arr1[i] * dx + arr2[i] * dy + i)
            # 更新答案
            ans = max(ans, maxv - minv)
        return ans