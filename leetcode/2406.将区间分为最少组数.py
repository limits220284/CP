from sortedcontainers import SortedList
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        s=SortedList(intervals)
        ans=0
        while s:
            l,r=0,len(s)-1
            t=0
            arr=[0]
            while l<len(s):
                r=len(s)-1
                while l<r:
                    mid=(l+r)//2
                    if s[mid][0]>s[t][1]:
                        r=mid
                    else:
                        l=mid+1
                if s[l][0]>s[t][1]:
                    arr.append(l)
                    t=l
                else:
                    break
            k=0
            for i in arr:
                s.pop(i-k)
                k+=1
            ans+=1
        return ans