func minPathCost(grid [][]int, moveCost [][]int) int {
    m, n := len(grid), len(grid[0])
    f := make([][]int, m)
    for i := 0; i < m; i++ {
        f[i] = make([]int, n)
    }
    for i := 0; i < m; i ++ {
        for j := 0; j < n; j ++ {
            f[i][j] = math.MaxInt / 2
        }
    }
    f[0] = grid[0]
    for i := 0; i < m - 1; i ++ {
        for j := 0; j < n; j ++ {
            for k := 0; k < n; k ++ {
                f[i + 1][k] = min(f[i + 1][k], f[i][j] + moveCost[grid[i][j]][k] + grid[i + 1][k])
            }
        }
    }
    return slices.Min(f[m - 1])
}