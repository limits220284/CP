func maximizeSum(nums []int, k int) int {
    sort.Ints(nums)
    m := nums[len(nums) - 1]
    return (k - 1 + m + m) * k / 2
}