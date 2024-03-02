class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # 格子最多围住的范围是多少？
        # 围住对角线即可，因为那么判断(0,0)能不能到达某个围不住的点，就一定能够到达target
        # 需要判断源点没有被围住，target没有被围住即可
        def dis(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        nb = len(blocked)
        blocked = set([tuple(x) for x in blocked])
        def check(source, target):
            flag = False
            q = deque([tuple(source)])
            vis = set([tuple(source)])
            while q:
                x, y = q.popleft()
                if [x, y] == target:
                    return True
                if dis(source, [x, y]) > nb:
                    flag = True
                    break
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= dx < 10 ** 6 and 0 <= dy < 10 ** 6 and (dx, dy) not in vis and (dx, dy) not in blocked:
                        vis.add((dx, dy))
                        q.append((dx, dy))
                if len(q) > (nb // 4) ** 2:
                    flag = True
                    break
            return flag
        return check(source, target) and check(target, source)