# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        #后序遍历
        dic=Counter(to_delete)
        res=[] if root.val in dic else[root]
        def dfs(root,parent,d):
            if not root:
                return root
            dfs(root.left,root,'左')
            dfs(root.right,root,'右')
            if root.val in dic:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                if d=='左':
                    parent.left=None
                if d=='右':
                    parent.right=None
        dfs(root,0,0)
        return res