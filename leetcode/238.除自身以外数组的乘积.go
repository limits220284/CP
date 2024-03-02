func productExceptSelf(nums []int) []int {
    n := len(nums)
    pre := make([]int, n+1)
    suf := make([]int, n+1)
    ans := make([]int, n)
    pre[0] = 1
    for i := 1; i < n; i++ {
        pre[i] = pre[i-1] * nums[i-1]
    }
    suf[n-1] = 1
    for i := n-2; i >= 0; i-- {
        suf[i] = suf[i+1] * nums[i+1]
    }
    for i := 0; i < n; i++ {
        ans[i] = pre[i] * suf[i]
    }
    return ans
}