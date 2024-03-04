class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mx=0
        dic=defaultdict(int)
        for x in nums:
            if x%2==0:
                dic[x]+=1
                mx=max(mx,dic[x])
        ans=1e5+1
        for x in dic:
            if dic[x]==mx:
                ans=min(ans,x)
        return -1 if ans==1e5+1 else ans