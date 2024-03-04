class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2*n
        ans = []
        t = []
        def dfs(i: int, left: int):
            if i == m:
                ans.append(''.join(t[::]))
                return
            if i-left < left:
                t.append(')')
                dfs(i+1, left)
                t.pop()
            if left < n:
                t.append('(')
                dfs(i+1, left+1)
                t.pop()
        dfs(0, 0)
        return ans