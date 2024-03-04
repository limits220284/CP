class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic=defaultdict(list)
        n=len(groupSizes)
        for i in range(n):
            dic[groupSizes[i]].append(i)
        res=[]
        for i,ans in dic.items():
            m=len(ans)
            j=0
            t=[]
            while j<m:
                t.append(ans[j])
                if len(t)==i:
                    res.append(t)
                    t=[]
                j+=1
        return res
            