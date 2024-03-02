class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x, y = location
        yuan = 0
        degrees = []
        for dx, dy in points:
            if dx == x:
                if dy > y:
                    degrees.append(90)
                elif dy < y:
                    degrees.append(270)
                else:
                    yuan += 1
            elif dx > x and dy >= y:
                alpha = (dy - y) / (dx - x)
                degrees.append(math.degrees(atan(alpha)))
            elif dx < x and dy >= y:
                alpha = (dy - y) / (x - dx)
                degrees.append(180 - math.degrees(atan(alpha)))
            elif dx < x and dy < y:
                alpha = (y - dy) / (x - dx)
                degrees.append(180 + math.degrees(math.atan(alpha)))
            elif dx > x and dy < y:
                alpha = (y - dy) / (dx - x)
                degrees.append(360 - math.degrees(math.atan(alpha)))
        degrees = degrees + [x + 360 for x in degrees]
        degrees.sort()
        l, r = 0, 0
        n = len(degrees)
        ans = 0
        while r < n:
            while degrees[r] - degrees[l] > angle:
                l += 1
            if r - l + 1 > ans:
                ans = max(ans, r - l + 1)
            r += 1
        return ans + yuan