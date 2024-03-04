class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans=0
        amount.sort()
        while amount[1]!=0:
            ans+=1
            amount[1]-=1
            amount[2]-=1
            amount.sort()
        return ans+amount[2]