class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        t = []
        n = len(s)
        def dfs(i: int):
            if i == n:
                ans.append(t[::])
                return
            for j in range(i, n):
                c = s[i:j+1]
                if c == c[::-1]:
                    t.append(c)
                    dfs(j+1)
                    t.pop()
        dfs(0)
        return ans