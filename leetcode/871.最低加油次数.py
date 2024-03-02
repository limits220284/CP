#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#

# @lc code=start
class Solution:
    # 贪心解法
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:return 0
        n = len(stations)
        heap = []
        remainOil = startFuel # 剩余的汽油
        pos = 0 # 经过的加油站
        res = 0 # 加油次数
        while remainOil < target: # 没油了
            while pos < n and remainOil >= stations[pos][0]: #可以到达这个加油站
                heappush(heap, -stations[pos][1]) # 带上这桶油
                pos += 1 # 这个加油站已经路过了
            if not heap: # 身上没油了
                return -1
            remainOil -= heappop(heap) # python 只有最小堆 这里是取负数
            res += 1 # 加油次数加一
        return res
    # 动态规划解法
    # def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # int[] dp = new int[stations.length + 1];
        # dp[0] = startFuel;
        # //遍历加油站
        # for (int i = 0; i < stations.length; i++) {
        #     //更新dp
        #     for (int j = i; j >= 0; j--) {
        #         //必须能达到此加油站才能更新dp[j]
        #         if (dp[j] >= stations[i][0]) {
        #             //判断加j+1次油（也就是加了j次+当前路过的这次油量）
        #             dp[j + 1] = Math.max(dp[j + 1], dp[j] + stations[i][1]);
        #         }
        #     }
        # }
        # //找到第一个大于等于target的 i，也就是加油次数
        # for (int i = 0; i <= stations.length; i++) {
        #     if (dp[i] >= target) {
        #         return i;
        #     }
        # }
        # return -1;
        
        

