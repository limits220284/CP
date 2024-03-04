class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vis_row=[[False for j in range(9)] for i in range(9)]
        vis_col=[[False for j in range(9)] for i in range(9)]
        vis_sqr=[[[False for k in range(9)] for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                else:
                    a=int(board[i][j])-1
                    if vis_row[i][a] or vis_col[j][a] or vis_sqr[i//3][j//3][a]:
                        return False
                    vis_row[i][a]=True
                    vis_col[j][a]=True
                    vis_sqr[i//3][j//3][a]=True
        return True
                    
                
                    
                
        