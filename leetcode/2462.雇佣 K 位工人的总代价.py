class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # 主要思想就是维护两个小根堆
        ans,n=0,len(costs)
        if candidates*2<n:
            pre=costs[:candidates]
            heapify(pre)
            suf=costs[-candidates:]
            heapify(suf)
            i,j=candidates,n-1-candidates
            while k and i<=j:
                if pre[0]<=suf[0]:
                    ans+=heapq.heappop(pre)
                    heapq.heappush(pre,costs[i])
                    i+=1
                else:
                    ans+=heapq.heappop(suf)
                    heapq.heappush(suf,costs[j])
                    j-=1
                k-=1
            costs=pre+suf
        costs.sort()
        return ans+sum(costs[:k])
                