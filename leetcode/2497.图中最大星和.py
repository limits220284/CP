class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # 建图
        n=len(vals)
        g=[[] for _ in range(n)]
        res=-inf
        for x,y in edges:
            g[x].append((y,vals[y]))
            g[y].append((x,vals[x]))
        for i,arr in enumerate(g):
            arr.sort(key=lambda x:x[1],reverse=True)
            tot=0
            for x in arr[0:k]:
                tot+=x[1] if x[1]>0 else 0
            tot+=vals[i]
            res=max(res,tot)
        return res