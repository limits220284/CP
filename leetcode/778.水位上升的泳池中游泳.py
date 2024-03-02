class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 这不就tm二分 + bfs
        # 或者是并查集，但是并查集比较难写
        n = len(grid)
        inx = [0, 0, 1, -1]
        iny = [1, -1, 0, 0]
        def check(mid):
            if grid[0][0] > mid: return False
            q = deque([(0, 0)])
            vis = {}
            vis[(0, 0)] = True
            while q:
                x, y = q.popleft()
                if x == n-1 and y == n-1:
                    return True
                for k in range(4):
                    dx, dy = x + inx[k], y + iny[k]
                    if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] <= mid and (dx, dy) not in vis:
                        q.append((dx, dy))
                        vis[(dx, dy)] = True
            return False
            
        l, r = 0, n ** 2
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
        