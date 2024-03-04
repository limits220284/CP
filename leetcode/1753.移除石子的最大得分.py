class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res, maxHeap = 0, [-a, -b, -c]
        heapify(maxHeap)
        while maxHeap:
            first, second, third = -heappop(maxHeap), -heappop(maxHeap), heappop(maxHeap)
            if second == 0 and third == 0:
                break
            res += 1
            first -= 1
            second -= 1
            heappush(maxHeap, -first)
            heappush(maxHeap, -second)
            heappush(maxHeap, third)
        return res
