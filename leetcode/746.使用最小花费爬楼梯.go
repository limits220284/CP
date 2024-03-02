// f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])
func minCostClimbingStairs(cost []int) int {
    n := len(cost)
    f := make([]int, n + 1)
    for i := 2; i <= n; i ++ {
        f[i] = f[i - 1] + cost[i - 1]
        f[i] = min(f[i], f[i - 2] + cost[i - 2])
    }
    return f[n]
}