func findTheCity(n int, edges [][]int, distanceThreshold int) int {
    //floyed 算法
    //f[i][j] = min(f[i][k] + f[k][j], f[i][j])
    f := make([][]int, n)
    for i := 0; i < n; i++ {
        f[i] = make([]int, n)
        for j := range f[i] {
            f[i][j] = math.MaxInt / 2
        }
    }
    for _, e := range edges {
        x, y, wt := e[0], e[1], e[2]
        f[x][y], f[y][x] = wt, wt
    }
    for k := 0; k < n; k++ {
        for i := 0; i < n; i++ {
            for j := 0; j < n; j++ {
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])
            }
        }
    }
    idx := -1
    mx := math.MaxInt
    for i := 0; i < n; i ++ {
        cnt := 0
        for j := 0; j < n; j ++ {
            if j != i && f[i][j] <= distanceThreshold {
                cnt += 1
            }
        }
        if cnt <= mx {
            mx = cnt
            idx = i
        }
    }
    return idx
}