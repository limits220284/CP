#
# @lc app=leetcode.cn id=1686 lang=python3
#
# [1686] 石子游戏 VI
#

# @lc code=start
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        arr = list(zip(aliceValues, bobValues))
        arr.sort(key = lambda x: (x[0] + x[1]), reverse =  True)
        suma = sumb = 0
        for i, socre in enumerate(arr):
            if i % 2 == 0:
                suma += socre[0]
            else:
                sumb += socre[1]
        if suma < sumb: return -1
        elif suma > sumb: return 1
        return 0
        
