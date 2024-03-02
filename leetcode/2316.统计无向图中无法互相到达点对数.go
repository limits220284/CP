func countPairs(n int, edges [][]int) int64 {
    g := make([][]int, n)
    vis := make([]bool, n)
    ans := []int{}
    for i := 0; i < n; i++ {
        g[i] = []int{}
    }
    for _, edge := range edges {
        x, y := edge[0], edge[1]
        g[x] = append(g[x], y)
        g[y] = append(g[y], x)
    }
    var dfs func(int) int
    dfs = func(x int) int {
        res := 1
        vis[x] = true
        for _, y := range g[x] {
            if vis[y]{
                continue
            }
            res += dfs(y)
        }
        return res
    }
    for i := 0; i < n; i++ {
        if !vis[i] {
            ans = append(ans, dfs(i))
        }
    }
    res := 0
    s := 0
    for _, x := range ans {
        res += x * s
        s += x
    }
    return int64(res)
}