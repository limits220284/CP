import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pri_que=[]
        for i in range(n):
            heapq.heappush(pri_que,nums[i])
            if len(pri_que)>k:
                heapq.heappop(pri_que)#总是吧当前最小的弹出去
        return heapq.heappop(pri_que)