# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic={}
        self.valid=False
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.dic.get(k-root.val):
                self.valid=True
            self.dic[root.val]=True
            dfs(root.right)
        dfs(root)
        return self.valid