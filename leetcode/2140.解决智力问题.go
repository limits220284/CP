func mostPoints(questions [][]int) int64 {
    n := len(questions)
    dp := make([]int, n + 1)
    for i := n - 1; i >= 0; i-- {
        dp[i] = max(dp[i + 1], questions[i][0] + dp[min(n, i + questions[i][1] + 1)])
    }
    return int64(dp[0])
}