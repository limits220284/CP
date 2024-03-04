class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        ans=[]
        for i in range(n):
            d,m=divmod(dist[i],speed[i])
            ans.append(d+1 if m else d)
        cnt=0
        ans.sort()
        for x in ans:
            if cnt>=x:
                return cnt
            cnt+=1
        return cnt