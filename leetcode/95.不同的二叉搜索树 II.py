class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(s, e):
            if s > e:
                return [None]
            ans = []
            for i in range(s, e + 1):
                ls = dfs(s, i-1)
                rs = dfs(i+1, e)
                for l in ls:
                    for r in rs:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        return dfs(1, n)
