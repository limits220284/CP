class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        eps = 1e-7
        alpha = 1.0
        # decay = 1e-3
        n = len(positions)
        x = sum(pos[0] for pos in positions) / n
        y = sum(pos[1] for pos in positions) / n
        
        def getDist(xc, yc):
            return sum(((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 for x, y in positions)
        
        while True:
            xPrev, yPrev = x, y
            dx, dy = 0.0, 0.0
            for i in range(n):
                pos = positions[i]
                dx += (x - pos[0]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps)
                dy += (y - pos[1]) / (sqrt((x - pos[0]) * (x - pos[0]) + (y - pos[1]) * (y - pos[1])) + eps)
            x -= alpha * dx
            y -= alpha * dy
            alpha *= 0.999
            if ((x - xPrev) ** 2 + (y - yPrev) ** 2) ** 0.5 < eps:
                break
        return getDist(x, y)