class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 模拟题目，最多执行4次 并进行检查即可
        cnt=0
        n=len(instructions)
        x,y=0,0
        d=0
        dx,dy=x,y
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        while cnt<4:
            for i in range(n):
                if instructions[i]=='G':
                    dx+=dir[d][0]
                    dy+=dir[d][1]
                elif instructions[i]=='L':
                    d=(d-1)%4
                else:
                    d=(d+1)%4
            if dx==x and dy==y:
                return True
            cnt+=1
        return False