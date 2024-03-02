func gardenNoAdj(n int, paths [][]int) []int {
    g := make([][]int, n + 1)
    for _, t := range paths {
        g[t[0]] = append(g[t[0]], t[1])
        g[t[1]] = append(g[t[1]], t[0])
    }
    ans := make([]int, n + 1)
    for i := 1; i <= n; i++ {
        mask := uint8(1)
        for _, y := range g[i] {
            mask |= (1 << ans[y])
        }
        ans[i] = bits.TrailingZeros8(^mask)
    }
    return ans[1:]
}