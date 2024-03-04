class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1])
        run = [False] * 2001
        for s, e, d in tasks:
            d -= sum(run[s:e+1])
            if d > 0:
                for i in range(e, s-1, -1):
                    if run[i]: continue
                    run[i] = True
                    d -= 1
                    if d == 0: break
        return sum(run)