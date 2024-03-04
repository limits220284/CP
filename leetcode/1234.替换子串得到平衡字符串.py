class Solution:
    def balancedString(self, s: str) -> int:
        # 滑动窗口
        n=len(s)
        k=n//4
        cnt=Counter(s)
        if cnt['Q']==k and cnt['W']==k and cnt['E']==k and cnt['R']==k:
            return 0
        # 双指针
        l,r=0,0
        ans=n
        while r<n:
            cnt[s[r]]-=1
            while cnt['Q']<=k and cnt['W']<=k and cnt['E']<=k and cnt['R']<=k:
                ans=min(ans,r-l+1)
                cnt[s[l]]+=1
                l+=1
            r+=1
        return ans