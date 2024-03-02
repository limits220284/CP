func reachableNodes(n int, edges [][]int, restricted []int) int {
    hsh := make(map[int]bool)
    for _, v := range restricted {
        hsh[v] = true
    }
    g := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        g[a] = append(g[a], b)
        g[b] = append(g[b], a)
    }
    fmt.Println(g)
    ans := 0
    var dfs func(int, int)
    dfs = func(x, fa int) {
        fmt.Println(x)
        ans += 1
        for _, y := range g[x] {
            if hsh[y] == false && y != fa {
                dfs(y, x)
            }
        }
    }
    dfs(0, -1)
    return ans
}