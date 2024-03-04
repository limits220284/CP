class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        #贪心
        intervals.sort(key=lambda x:(x[0],-x[1]))
        n=len(intervals)
        cnt=0
        a,b=1e8+1,1e8+2
        for i in range(n-1,-1,-1):
            s,e=intervals[i][0],intervals[i][1]
            if b<=e:
                continue
            elif a>e:
                a,b=s,s+1
                cnt+=2
            elif a<=e:
                a,b=s,a
                cnt+=1
        return cnt