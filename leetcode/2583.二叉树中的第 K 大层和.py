# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        que = deque([root])
        arr = []
        while que:
            n = len(que)
            tot = 0
            for i in range(n):
                a = que.popleft()
                tot += a.val
                if a.left:
                    que.append(a.left)
                if a.right:
                    que.append(a.right)
            arr.append(tot)
        arr.sort(reverse = True)
        if len(arr) < k:
            return -1
        return arr[k-1]
        