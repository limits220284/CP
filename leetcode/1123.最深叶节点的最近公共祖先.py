# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return 0, None
            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)
            if left_height > right_height:
                return left_height + 1, left_lca
            if left_height < right_height:
                return right_height + 1, right_lca
            return left_height + 1, node
        return dfs(root)[1]