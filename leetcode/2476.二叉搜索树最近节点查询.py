class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(o):
            if not o:return 
            dfs(o.left)
            ans.append(o.val)
            dfs(o.right)
        dfs(root)
        res=[]
        for x in queries:
            j=bisect_left(ans,x)
            mx=ans[j] if j<len(ans) else -1
            j=bisect_right(ans,x)
            mi=ans[j-1] if j else -1
            res.append([mi,mx])
        return res