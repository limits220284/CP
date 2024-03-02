class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # f[i]代表组成i的总数
        # 换个思路理解，相当于爬楼梯，每次能够爬的就是nums层数
        # 所有的组合的结果就是爬的顺序，比如爬四层，可以先爬2，然后再爬1，1
        # 定义的f[i][j]为组合长度为i的情况下，满足j的个数
        # f[i][j] = sum(f[i-1][j-nums[0]], f[i-1][j-nums[1]])
        ans = 0
        f = [[0] * (target + 1) for _ in range(target+1)]
        f[0][0] = 1
        for i in range(1, target + 1):
            for j in range(target+1):
                for x in nums:
                    if j >= x:
                        f[i][j] += f[i-1][j-x]
            ans += f[i][target]
        return ans
        
