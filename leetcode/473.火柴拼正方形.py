class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        tLen = totalLen // 4

        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                # 如果当前不在s中, 继续
                if s & (1 << k) == 0:
                    continue
                # 找到上一个状态
                s1 = s - (1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= tLen:
                    # 之所以要mod tLen是因为dp[s]在s1的基础上加上了一条边, 当前可以为零
                    dp[s] = (dp[s1] + v) % tLen
        return dp[-1] == 0
