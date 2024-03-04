# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.dic={}
    def numColor(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dic[root.val]=True
        self.numColor(root.left)
        self.numColor(root.right)
        return len(self.dic.keys())
