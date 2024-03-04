# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 采用先找出每一层的节点，然后反转，然后再构造二叉树
        q=deque([root])
        t=-1
        tot=[]
        while q:
            t+=1
            n=len(q)
            for i in range(n):
                ans=q.popleft()
                tot.append(ans.val)
                if ans.left:
                    q.append(ans.left)
                if ans.right:
                    q.append(ans.right)
            if t%2==1:
                tot[-2**t:]=tot[-2**t:][::-1]
        #构造树
        n=len(tot)
        head=TreeNode(tot[0])
        q=deque([head])
        j=1
        while q and j<n:
            m=len(q)
            for i in range(m):
                ans=q.popleft()
                ans.left=TreeNode(tot[j])
                j+=1
                q.append(ans.left)
                ans.right=TreeNode(tot[j])
                q.append(ans.right)
                j+=1
        return head
