func minCost(nums []int, x int) int64 {
    // 直接计算出所有情况下的成本   
    n := len(nums)
    f := make([][]int, n)
    for i, _ := range f {
        f[i] = make([]int, n)
    }
    f[0] = nums
    sum := func(arr []int) int {
        res := 0
        for _, x := range arr {
            res += x
        }
        return res
    }
    ans := sum(nums)
    mi := make([]int, n)
    copy(mi, nums)
    for i := 1; i < n; i++ {
        for j := 0; j < n; j++ {
            f[i][j] = f[i - 1][(j + 1) % n]
            mi[j] = min(mi[j], f[i][j])
        }
        ans = min(ans, sum(mi) + i * x)
    }
    return int64(ans)
}