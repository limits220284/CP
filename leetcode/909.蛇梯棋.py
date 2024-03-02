#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        gate = defaultdict(int)
        for i in range(m-1, -1, -1):
            for j in range(n):
                if board[i][j] != -1:
                    gate[(m-1-i) * n + (j+1 if (m-i-1) % 2 == 0 else (n-j))] = board[i][j]
        q =deque([(1, 0)])
        vis = set([1])
        while q:
            tot = len(q)
            for i in range(tot):
                t, dep = q.popleft()
                for j in range(t + 1, min(t + 6, n ** 2) + 1):
                    nxt = j
                    if j in gate:
                        nxt = gate[j]
                    if nxt == n ** 2:
                        return dep + 1
                    if nxt not in vis:
                        q.append((nxt, dep + 1))
                        vis.add(nxt)
        return -1

