# 要学会转化问题
# 如果一个人可以看到其右边的人，就代表着左边的人不能将其挡住
# 需要维护一个单调递增的序列
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stk = [inf]
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            cnt = 0
            while stk and heights[i] >= stk[-1]:
                stk.pop()
                cnt += 1
            if len(stk) > 1: cnt += 1  
            ans[i] = cnt
            stk.append(heights[i])
        return ans