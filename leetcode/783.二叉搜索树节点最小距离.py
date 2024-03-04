# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre=-1e5
        self.mi=1e5
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        #中序遍历
        def dfs(root):
            if not root:
                return
            self.minDiffInBST(root.left)
            self.mi=min(int(abs(root.val-self.pre)),self.mi)
            self.pre=root.val
            self.minDiffInBST(root.right)
        dfs(root)
        return self.mi