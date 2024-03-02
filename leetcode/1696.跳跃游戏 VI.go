func maxResult(nums []int, k int) int {
    // f[i] = max(f[i-1], f[i-2], ..., f[i - k]) + nums[i]
    n := len(nums)
    q := make([]int, 0)
    f := make([]int, n)
    f[0] = nums[0]
    q = append(q, 0)
    for i := 1; i < n; i ++ {
        f[i] = f[q[0]] + nums[i]
        for len(q) > 0 && f[i] >= f[q[len(q) - 1]] {
            q = q[: len(q) - 1]
        }
        q = append(q, i)
        if q[0] <= i - k {
            q = q[1:]
        }
    }
    return f[len(f) - 1]
}