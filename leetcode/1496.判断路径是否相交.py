class Solution:
    def isPathCrossing(self, path: str) -> bool:
        n=len(path)
        x,y=0,0
        dic=set([(x,y)])
        for c in path:
            if c=='N':
                x,y=x,y-1
            elif c=='E':
                x,y=x+1,y
            elif c=='S':
                x,y=x,y+1
            else:
                x,y=x-1,y
            if (x,y) in dic:
                return True
            dic.add((x,y))
        return False
            