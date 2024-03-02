"""
定义状态(idx, cnt), idx表示当前位置，cnt表示连续往后面跳了几次
- 注意设定上界, 要保证超过x还能跳回来
- 下界不能够跳成负数
- 采用vis记录状态
"""
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, target: int) -> int:
        up = max(max(forbidden) + a, target) + b
        forbidden = Counter(forbidden)
        q = deque([(0, 0)])
        vis = set()
        step = 0
        while q:
            m = len(q)
            for _ in range(m):
                x, cnt = q.popleft()
                if x == target:
                    return step
                dx = x + a
                if 0 <= dx <= up and (dx, 0) not in vis and dx not in forbidden:
                    vis.add((dx, 0))
                    q.append((dx, 0))
                dx = x - b
                if 0 <= dx <= up and (dx, cnt + 1) not in vis and dx not in forbidden:
                    if cnt < 1:
                        vis.add((dx, cnt + 1))
                        q.append((dx, cnt + 1))
            step += 1
        return -1