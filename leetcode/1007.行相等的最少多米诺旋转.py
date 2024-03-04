class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n=len(tops)
        ans=[[0,0,0] for j in range(7)]
        for i in range(n):
            if tops[i]!=bottoms[i]:
                ans[bottoms[i]][1]+=1
                ans[bottoms[i]][2]+=1
            else:
                ans[tops[i]][1]+=1
            ans[tops[i]][0]+=1
            ans[tops[i]][2]+=1
        res=n
        for x in ans:
            if x[2]==n:
                res=min(res,min(x[0],x[1])-(x[0]+x[1]-x[2]))
        if res==n:
            return -1
        return res
