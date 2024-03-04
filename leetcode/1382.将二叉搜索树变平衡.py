# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        #二叉搜索树有二叉搜索树的解法
        #1.先找到数组
        #2.二分递归进行构造
        ans=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        n=len(ans)
        def build(l,r):
            if l>r:
                return None
            mid=l+(r-l)//2
            left=build(l,mid-1)
            right=build(mid+1,r)
            return TreeNode(ans[mid],left,right)
        return build(0,n-1)
        