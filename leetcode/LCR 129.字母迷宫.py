class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[False] * n for _ in range(m)]
        def dfs(x, y, cnt):
            if board[x][y] != word[cnt]:
                return False
            if cnt == len(word) - 1:
                return True
            vis[x][y] = True
            res = False
            for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if dx>=0 and dx<m and dy>=0 and dy<n and not vis[dx][dy]:
                    if dfs(dx, dy, cnt+1):
                        res = True
                        break
            vis[x][y] = False
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False