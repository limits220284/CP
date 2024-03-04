class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt=Counter()
        mx=0
        l,r,n=0,0,len(fruits)
        while r<n:
            cnt[fruits[r]]+=1
            while len(cnt)>2:
                cnt[fruits[l]]-=1
                if cnt[fruits[l]]==0:
                    cnt.pop(fruits[l])
                l+=1
            mx=max(mx,r-l+1)
            r+=1
        return mx