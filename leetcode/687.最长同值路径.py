# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            left1=left if root.left and root.val==root.left.val else 0
            right1=right if root.right and root.val==root.right.val else 0
            nonlocal ans
            ans=max(ans,left1+right1)
            return max(left1,right1)+1
        dfs(root)
        return ans
