#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 树形dp
        # f代表选择当前的这个节点的最大值，g代表不选择当前这个节点的最大值,采用hash进行存储
        # f[node] = max(g[node.left] + node.val, g[node.right] + node.val)
        # g[node] = max(f[node.left], g[node.left]) + max(f[node.right], g[node].right)
        def dfs(node):
            if node == None:
                return 0, 0
            lf, lg = dfs(node.left)
            rf, rg = dfs(node.right)
            f = lg + rg + node.val
            g = max(lf, lg) + max(rf, rg)
            return f, g
        f, g = dfs(root)
        return  max(f, g)