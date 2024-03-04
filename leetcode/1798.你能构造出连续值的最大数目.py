class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # 贪心算法
        coins.sort()
        x=0
        for y in coins:
            if y<=x+1:
                x=x+y
            else:
                break
        return x+1