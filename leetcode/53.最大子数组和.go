func maxSubArray(nums []int) int {
    // 动态规划
    // dp[i] = max(dp[i - 1], dp[i - 1] + nums[i])
    // return max(dp)
    n := len(nums)
    f := make([]int, n)
    ans := nums[0]
    f[0] = nums[0]
    for i := 1; i < n; i ++ {
        f[i] = max(nums[i], f[i - 1] + nums[i])
        ans = max(ans, f[i])
    }
    return ans
}