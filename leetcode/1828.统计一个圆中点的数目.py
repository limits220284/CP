class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def check(x,y,a,b,r):
            return (x-a)**2+(y-b)**2<=r**2
        ans=[]
        for a,b,r in queries:
            cnt=0
            for x,y in points:
                if check(x,y,a,b,r):
                    cnt+=1
            ans.append(cnt)
        return ans
                
            




        