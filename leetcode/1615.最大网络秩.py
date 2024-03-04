class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic=[set() for i in range(n)]
        if len(roads)==0:
            return 0
        for road in roads:
            dic[road[0]].add(road[1])
            dic[road[1]].add(road[0])
        graph=copy.deepcopy(dic)
        st=list(set([len(x) for x in dic]))
        st.sort(reverse=True)
        mx=st[0]
        mx_1=-1
        if len(st)!=1:
            mx_1=st[1]
        ans_mx=[]
        ans_mx_1=[]
        for i,x in enumerate(graph):
            if len(x)==mx:
                ans_mx.append(i)
            elif len(x)==mx_1:
                ans_mx_1.append(i)
        res=0
        if len(ans_mx)>=2:
            for i in range(len(ans_mx)):
                for j in range(i+1,len(ans_mx)):
                    if ans_mx[i] in graph[ans_mx[j]]:
                        res=max(res,2*mx-1)
                    else:
                        res=max(res,2*mx)
        else:
            for i in range(len(ans_mx_1)):
                if ans_mx[0] in graph[ans_mx_1[i]]:
                    res=max(res,mx+mx_1-1)
                else:
                    res=max(res,mx+mx_1)
        return res