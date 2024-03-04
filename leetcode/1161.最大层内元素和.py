# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        que=deque()
        que.appendleft(root)
        res=-1e9
        fl=0
        dep=0
        while que:
            n=len(que)
            ans=0
            dep+=1
            for i in range(n):
                a=que.pop()
                ans+=a.val
                if a.left:
                    que.appendleft(a.left)
                if a.right:
                    que.appendleft(a.right)
            if ans>res:
                res=ans
                fl=dep
        return fl