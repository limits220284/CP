class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # 维护一个大根堆和一个小根堆
        Mod=10**9+7
        buy_q=[]
        sell_q=[]
        for p,m,t in orders:
            if t==0:
                while sell_q and p>=sell_q[0][0]:
                    if m>=sell_q[0][1]:
                        m-=sell_q[0][1]
                        heappop(sell_q)
                    else:
                        sell_q[0][1]-=m
                        m-=m
                        break
                if m:
                    heappush(buy_q,[-p,m])
            else:
                while buy_q and p<=abs(buy_q[0][0]):
                    if m>=buy_q[0][1]:
                        m-=buy_q[0][1]
                        heappop(buy_q)
                    else:
                        buy_q[0][1]-=m
                        m-=m
                        break
                if m:
                    heappush(sell_q,[p,m])
        ans=0
        for _,m in sell_q:
            ans=(ans+m)%Mod
        for _,m in buy_q:
            ans=(ans+m)%Mod
        return ans