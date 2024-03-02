# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 寻找子问题，左子树最长路径和，右子树最长路径
        ans = -inf
        def dfs(root):
            nonlocal ans
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            ans = max(ans, l + root.val, r + root.val, l + r + root.val, root.val)
            return max(l + root.val, r + root.val, root.val)
        dfs(root)
        return ans