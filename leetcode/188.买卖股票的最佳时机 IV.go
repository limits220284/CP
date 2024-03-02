func maxProfit1(k int, prices []int) int {
    n := len(prices)
    memo := make([][][2]int, n)
    for i := range memo {
        memo[i] = make([][2]int, k+1)
        for j := range memo[i] {
            memo[i][j] = [2]int{-1, -1} // -1 表示还没有计算过
        }
    }
    var dfs func(int, int, int) int
    dfs = func(i, j, hold int) (res int) {
        if j < 0 {
            return math.MinInt / 2 // 防止溢出
        }
        if i < 0 {
            if hold == 1 {
                return math.MinInt / 2
            }
            return
        }
        p := &memo[i][j][hold]
        if *p != -1 { // 之前计算过
            return *p
        }
        defer func() { *p = res }() // 记忆化
        if hold == 1 {
            return max(dfs(i-1, j, 1), dfs(i-1, j-1, 0)-prices[i])
        }
        return max(dfs(i-1, j, 0), dfs(i-1, j, 1)+prices[i])
    }
    return dfs(n-1, k, 0)
}
func maxProfit(k int, prices []int) int {
    n := len(prices)
    f := make([][][2]int, n+1)
    for i := range f{
        f[i] = make([][2]int, k+2)
        for j := range f[i]{
            f[i][j] = [2]int{math.MinInt / 2, math.MinInt / 2}
        }
    }
    for j := 1; j <= k+1; j++{
        f[0][j][0] = 0
    }
    for i, p := range prices{
        for j := 1; j <= k+1; j++{
            f[i+1][j][0] = max(f[i][j][0], f[i][j][1] + p)
            f[i+1][j][1] = max(f[i][j][1], f[i][j-1][0] - p)
        }
    }
    return f[n][k+1][0]
}
func max(a, b int) int { if a < b { return b }; return a }