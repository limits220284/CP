# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(root,cnt):
            if not root:
                return root
            if cnt==depth-1:
                left=TreeNode(val,root.left,None)
                right=TreeNode(val,None,root.right)
                return TreeNode(root.val,left,right)
            root.left=dfs(root.left,cnt+1)
            root.right=dfs(root.right,cnt+1)
            return root
        if depth==1:
            ans=TreeNode(val,root,None)
            return ans
        return dfs(root,1)