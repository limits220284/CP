class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #直接遍历？感觉不太行的样子
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                cnt=0
                for x in range(3):
                    for y in range(3):
                        dx,dy=i+1-x,j+1-y
                        if dx>=0 and dx<m and dy>=0 and dy<n and (dx!=i or dy!=j):
                            if board[dx][dy]==1 or board[dx][dy]==-1:
                                cnt+=1
                if board[i][j]==1:
                    if cnt<2 or cnt>3:
                        board[i][j]=-1
                elif cnt==3:
                    board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1:
                    board[i][j]=0
                if board[i][j]==2:
                    board[i][j]=1





