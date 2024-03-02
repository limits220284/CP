func maxSelectedElements(nums []int) int {
    // dp[i]表示以i为结尾的最长长度
    // 
    dp := make(map[int]int)
    sort.Ints(nums)
    mx := 0
    for _, num := range nums {
        dp[num + 1] = max(dp[num + 1], dp[num] + 1)
        dp[num] = max(dp[num], dp[num - 1] + 1)
        mx = max(max(mx, dp[num]), dp[num + 1])
    }
    return mx
}