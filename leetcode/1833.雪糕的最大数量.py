class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        for x in costs:
            if coins>=x:
                coins-=x
                ans+=1
            else:
                break
        return ans