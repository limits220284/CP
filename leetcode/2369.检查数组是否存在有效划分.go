func validPartition(nums []int) bool {
    n := len(nums)
    f := make([]int, n + 1)
    f[0] = 1
    for i := 0; i < n; i ++ {
        if i >= 1 && nums[i] == nums[i - 1] && f[i - 1] == 1{
            f[i + 1] = 1
            continue
        }
        if i >= 2 && nums[i] == nums[i - 1] && nums[i - 1] == nums[i - 2] && f[i - 2] == 1 {
            f[i + 1] = 1
            continue
        }
        if i >= 2 && nums[i] == nums[i - 1] + 1 && nums[i - 1] == nums[i - 2] + 1 && f[i - 2] == 1{
            f[i + 1] = 1
            continue
        }
    }
    return f[n] == 1
}