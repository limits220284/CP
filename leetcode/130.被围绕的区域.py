class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        #if m==n==1 and board[0][0]=='O':
            
        inx=[0,1,0,-1]
        iny=[1,0,-1,0]
        def dfs(x,y):
            for i in range(4):
                dx,dy=x+inx[i],y+iny[i]
                if dx>=0 and dx<m and dy>=0 and dy<n:
                    if board[dx][dy]=='O':
                        board[dx][dy]='#'
                        dfs(dx,dy)
        
        cnt=1
        circle=0
        x,y=0,0
        if board[x][y]=='O':
            board[x][y]='#'
            dfs(x,y)
        while cnt<2*(m+n)-4:
            dx,dy=x+inx[circle],y+iny[circle]
            while dx>=0 and dx<m and dy>=0 and dy<n:
                if board[dx][dy]=='O':
                    board[dx][dy]='#'
                    dfs(dx,dy)
                cnt+=1
                x,y=dx,dy
                dx,dy=x+inx[circle],y+iny[circle]
            circle+=1
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
                
            