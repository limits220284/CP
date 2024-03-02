#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 单调zhan解法
        # 贡献法
        MOD = 10 ** 9 + 7
        n = len(arr)
        left, right = [0] * n, [0] * n
        stk = []
        for i in range(n-1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            right[i] = n if not stk else stk[-1]
            stk.append(i)
        stk = []
        ans = 0
        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            left = -1 if not stk else stk[-1]
            stk.append(i)
            ans = (ans + arr[i] * (right[i] - i) * (i - left)) % MOD
        return ans % MOD
            
        
