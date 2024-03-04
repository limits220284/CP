class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt=0
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    cnt+=1
                    dy=j+1
                    while dy<n and board[i][dy]=="X":
                        board[i][dy]="."
                        dy+=1
                    dx=i+1
                    while dx<m and board[dx][j]=="X":
                        board[dx][j]="."
                        dx+=1
        return cnt
                        