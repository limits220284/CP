class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        edg=[p1,p2,p3,p4]
        cnt=0
        for i in range(4):
            ans=[]
            for j in range(4):
                if j==i:
                    continue
                ans.append([edg[j][0]-edg[i][0],edg[j][1]-edg[i][1]])
            for m in range(3):
                for n in range(m+1,3):
                    if ans[m][0]*ans[n][0]+ans[m][1]*ans[n][1]==0:
                        if ans[m][0]**2+ans[m][1]**2==ans[n][0]**2+ans[n][1]**2:
                            cnt+=1
        return cnt==4
                            
                        