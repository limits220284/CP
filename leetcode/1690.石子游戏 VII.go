func stoneGameVII(stones []int) int {
    n := len(stones)
    prefix := make([]int, n + 1)
    for i, x := range stones {
        prefix[i + 1] = prefix[i] + x
    }
    f := make([][]int, n)
    for i := 0; i < n; i ++ {
        f[i] = make([]int, n)
    }
    for i := n - 1; i >= 0; i -- {
        for j := i + 1; j < n; j ++ {
            f[i][j] = max(prefix[j + 1] - prefix[i + 1] - f[i + 1][j], prefix[j] - prefix[i] - f[i][j - 1])
        }
    }
    return f[0][n-1]
}