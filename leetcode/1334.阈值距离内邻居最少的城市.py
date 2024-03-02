import numpy as np
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        fr, to, we = np.split(np.asarray(edges), 3, -1)
        W = np.full((n, n), inf)
        W[fr, to] = we
        W[to, fr] = we
        W[range(n), range(n)] = 0
        print(W)
        for k in range(n): W = np.minimum(W, W[:, [k]] + W[[k], :])

        V = (W <= distanceThreshold).sum(-1)

        i = 0
        for j, m in enumerate(V):
            if m <= n:
                i, n = j, m

        return i

