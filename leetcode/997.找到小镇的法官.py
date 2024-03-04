class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp=[[0,0] for i in range(n+1)]
        for edge in trust:
            mp[edge[0]][1]+=1
            mp[edge[1]][0]+=1
        for i in range(1,n+1):
            if mp[i][0]==n-1 and mp[i][1]==0:
                return i
        return -1
        
        