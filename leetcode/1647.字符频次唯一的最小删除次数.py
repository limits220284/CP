class Solution:
    def minDeletions(self, s: str) -> int:
        dic=defaultdict(int)
        for c in s:
            dic[c]+=1
        ans=list(dic.values())
        ans.sort(reverse=True)
        cnt=0
        n=len(ans)
        for i in range(1,n):
            if ans[i]<ans[i-1]:
                continue
            elif ans[i-1]==0:
                cnt+=ans[i]
                ans[i]=0
            else:
                cnt+=ans[i]-(ans[i-1]-1)
                ans[i]=ans[i-1]-1
        return cnt
                