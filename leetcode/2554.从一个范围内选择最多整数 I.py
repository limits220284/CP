class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        dic=Counter(banned)
        ans=0
        tot=0
        for i in range(1,n+1):
            if i in dic:
                continue
            if tot+i<=maxSum:
                ans+=1
                tot+=i
            else:
                break
        return ans
            