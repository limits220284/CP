# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root,dir):
            sum=0
            if not root.left and not root.right and dir==1:
                sum+=root.val
                return sum
            if root.left:
                sum+=dfs(root.left,1)
            if root.right:
                sum+=dfs(root.right,0)
            return sum
        if not root.left and not root.right:
            return 0
        return dfs(root,0)
            
