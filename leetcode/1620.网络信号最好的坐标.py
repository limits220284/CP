# https://space.bilibili.com/206214
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        x_max = max(t[0] for t in towers)
        y_max = max(t[1] for t in towers)
        cx = cy = max_quality = 0
        for x in range(x_max + 1):
            for y in range(y_max + 1):
                quality = 0
                for tx, ty, q in towers:
                    d = (x - tx) * (x - tx) + (y - ty) * (y - ty)
                    if d <= radius * radius:
                        quality += int(q / (1 + d ** 0.5))
                if quality > max_quality:
                    cx, cy, max_quality = x, y, quality
        return [cx, cy]