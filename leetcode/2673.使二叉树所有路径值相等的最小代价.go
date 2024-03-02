func minIncrements(n int, cost []int) int {
    cost = append([]int{0:0}, cost...)
    fmt.Print(cost)
    n = len(cost)
    ans := 0
    var dfs func(int) int
    dfs = func(x int) int {
        if 2 * x >= n {
            return cost[x]
        }
        l := dfs(2 * x)
        r := dfs(2 * x + 1)
        ans += max(l, r) - min(l, r)
        return max(l, r) + cost[x]
    }
    dfs(1)
    return ans
}