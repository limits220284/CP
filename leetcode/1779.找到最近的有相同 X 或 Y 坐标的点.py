class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n=len(points)
        res=-1
        dis=float('inf')
        for i in range(n):
            if points[i][0]==x or points[i][1]==y:
                if abs(points[i][0]-x)+abs(points[i][1]-y)<dis:
                    dis=abs(points[i][0]-x)+abs(points[i][1]-y)
                    res=i   
        return res                