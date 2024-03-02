class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 折半枚举
        # 1 1 2 4 7 8
        # 2 7 8
        # 最接近的两块进行粉碎
        n = len(stones)
        mx = sum(stones) // 2
        # f[i][j] 表示前i个元素，背包容量最大为j能装多少
        # f[i][j] = max(f[i][j], f[i-1][j], f[i-1][j-nums[i]] + nums[i])
        f = [[0] * (mx + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(mx + 1):
                f[i][j] = f[i-1][j]
                if j >= stones[i-1]:
                    f[i][j] = max(f[i][j], f[i-1][j - stones[i-1]] + stones[i-1])
        return sum(stones) - 2 * f[n][mx]