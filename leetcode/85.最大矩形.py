#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        up = [[0] * n for _ in range(m+1)]
        left = [0] * n
        ans = 0
        for i in range(1, m+1):
            stk = []
            for j in range(n):
                if matrix[i-1][j] == "0":
                    up[i][j] = 0
                else: up[i][j] = up[i-1][j] + 1
                while stk and up[i][stk[-1]] >= up[i][j]:
                    stk.pop()
                if not stk: left[j] = -1
                else: left[j] = stk[-1]
                stk.append(j)
            stk = []
            for j in range(n-1, -1, -1):
                r = 0
                while stk and up[i][stk[-1]] >= up[i][j]:
                    stk.pop()
                if not stk: r = n
                else: r = stk[-1]
                stk.append(j)
                ans = max(ans, (r - left[j] - 1) * up[i][j])
        return ans
                
                
        