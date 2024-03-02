class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        ans = False
        vis = [[False] * n for _ in range(m)]
        def dfs(i, j, step):
            nonlocal ans
            if not (0 <= i < m and 0 <= j < n and not vis[i][j]):
                return
            if word[step] != board[i][j]:
                return
            if step == len(word) - 1 and board[i][j] == word[step]:
                ans = True
                return
            vis[i][j] = True
            dfs(i + 1, j, step + 1)
            dfs(i - 1, j, step + 1)
            dfs(i, j + 1, step + 1)
            dfs(i, j - 1, step + 1)
            vis[i][j] = False

        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)
                if ans:
                    return ans
        return ans   