import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for x in nums:
            dic[x]=dic.get(x,0)+1
        pri_que=[]
        for x,y in dic.items():
            heapq.heappush(pri_que,(y,x))
            if len(pri_que)>k:
                heapq.heappop(pri_que)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(pri_que)[1])
        return res