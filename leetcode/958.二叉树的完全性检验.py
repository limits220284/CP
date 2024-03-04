# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        cnt,mx=0,0
        def dfs(root,k):
            nonlocal cnt,mx
            if not root:
                return 
            cnt+=1
            mx=max(mx,k)
            dfs(root.left,2*k)
            dfs(root.right,2*k+1)
        dfs(root,1)
        return cnt==mx   
        
