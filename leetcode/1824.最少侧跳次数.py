class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        d = [1, 0, 1]
        for i in range(1, len(obstacles)):
            minCnt = inf
            for j in range(3):
                if j == obstacles[i] - 1:
                    d[j] = inf
                else:
                    minCnt = min(minCnt, d[j])
            for j in range(3):
                if j != obstacles[i] - 1:
                    d[j] = min(d[j], minCnt + 1)
        return min(d)