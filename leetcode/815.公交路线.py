#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#

# @lc code=start
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source: return 0
        station  = defaultdict(set)
        n = len(routes)
        g = [set() for _ in range(n)]
        for i, route in enumerate(routes):
            for x in route:
                for line in station[x]:
                    g[i].add(line)
                    g[line].add(i)
                station[x].add(i)
        vis = [False] * n
        q = deque()
        for line in station[source]:
            q.append(line)
            vis[line] = True
        ans = 1
        while q:
            m = len(q)
            for i in range(m):
                t = q.popleft()
                if t in station[target]:
                    return ans
                for v in g[t]:
                    if not vis[v]:
                        q.append(v)
                        vis[v] = True
            ans += 1
        return -1
            
