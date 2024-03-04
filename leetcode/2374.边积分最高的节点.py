class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        mi=1e5+1
        fo=0
        n=len(edges)
        dic=[0 for i in range(n)]
        for i in range(n):
            dic[edges[i]]+=i
            if dic[edges[i]]>fo:
                fo=dic[edges[i]]
                mi=edges[i]
            elif dic[edges[i]]==fo:
                mi=min(mi,edges[i])
        return mi