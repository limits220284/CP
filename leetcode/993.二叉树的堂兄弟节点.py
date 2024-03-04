# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.x_f=None
        self.y_f=None
        self.x_c=-1
        self.y_c=-2
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(root,cnt):
            if not root:
                return
            if root.left:
                if root.left.val==x:
                    self.x_f=root
                    self.x_c=cnt
                if root.left.val==y:
                    self.y_f=root
                    self.y_c=cnt
            if root.right:
                if root.right.val==x:
                    self.x_f=root
                    self.x_c=cnt
                if root.right.val==y:
                    self.y_f=root
                    self.y_c=cnt
            dfs(root.left,cnt+1)
            dfs(root.right,cnt+1)
        dfs(root,0)
        return self.x_c==self.y_c and self.x_f!=self.y_f
            