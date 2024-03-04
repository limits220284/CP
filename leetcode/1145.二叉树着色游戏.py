# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        xNode=None
        def dfs(root):
            if not root:
                return 0
            if root.val==x:
                nonlocal xNode
                xNode=root
            return dfs(root.left)+dfs(root.right)+1
        # 找到x树总节点个数
        dfs(root)
        cntl=dfs(xNode.left)
        cntr=dfs(xNode.right)
        if cntl>n//2 or cntr>n//2 or cntl+cntr+1<=n//2:
            return True
        return False