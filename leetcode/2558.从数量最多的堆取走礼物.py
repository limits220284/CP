class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        que=[]
        for g in gifts:
            heapq.heappush(que,-g)
        while k:
            a=que[0]
            heappop(que)
            heappush(que,-math.floor(math.sqrt(-a)))
            k-=1
        return -sum(que)