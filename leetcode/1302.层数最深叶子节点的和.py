# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # 层序优先遍历
        que=deque()
        que.append(root)
        res=0
        while que:
            n=len(que)
            res=0
            for i in range(n):
                ans=que.pop()
                if ans.left:
                    que.appendleft(ans.left)
                if ans.right:
                    que.appendleft(ans.right)
                res+=ans.val
        return res
                