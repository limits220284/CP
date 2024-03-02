# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 一边遍历一边维护一个最大值，如果最大值大于该节点的值，则代表不是一个好节点
        ans = 0
        def dfs(root, mx):
            if not root: return 
            nonlocal ans
            if mx <= root.val:
                ans += 1
            dfs(root.left, max(mx, root.val))
            dfs(root.right, max(mx, root.val))
        dfs(root, -inf)
        return ans