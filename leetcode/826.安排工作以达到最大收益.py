class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 排序 + 二分
        worker.sort()
        dp = list(zip(difficulty, profit))
        dp.sort()
        # 采用堆来维护前多少个元素的最大值即可
        h = []
        ans = 0
        idx = 0
        for i in range(len(worker)):
            while idx < len(dp) and dp[idx][0] <= worker[i]:
                heappush(h, -dp[idx][1])
                idx += 1
            if len(h):
                ans -= h[0]
        return ans