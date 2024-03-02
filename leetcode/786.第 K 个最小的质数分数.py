class Frac:
    def __init__(self, idx, idy, x, y):
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y
    def __lt__(self, other: "Frac") -> bool:
        return self.x * other.y < self.y * other.x
        
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        h = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapify(h)
        for _ in range(k - 1):
            t = heappop(h)
            idx, idy = t.idx, t.idy
            if idx + 1 < idy:
                heappush(h, Frac(idx + 1, idy, arr[idx + 1], arr[idy]))
        return [h[0].x, h[0].y]