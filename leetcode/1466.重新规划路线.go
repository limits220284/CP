func minReorder(n int, connections [][]int) int {
    g := make([][]int, n)
    vis := make(map[[2]int]bool)

    for _, connection := range connections {
        x, y := connection[0], connection[1]
        g[x] = append(g[x], y)
        g[y] = append(g[y], x)
        vis[[2]int{x, y}] = true
    }

    var dfs func(x, fa int) int
    dfs = func(x, fa int) int {
        t := 0
        for _, y := range g[x] {
            if y != fa {
                t += dfs(y, x)
                if vis[[2]int{x, y}] {
                    t++
                }
            }
        }
        return t
    }

    return dfs(0, -1)
}