// 如果k == 1, n == 1 返回-1
// 如果k == 1, n > 1 返回nums[1]
// 如果k > 1, n == 1, 如果k是奇数，返回-1，如果k是偶数，返回nums[0]
// 如果k > 1, n > 1, 返回前k - 1个数字中的最大值或者是nums[k]
func maximumTop(nums []int, k int) int {
    n := len(nums)
    mx := -1
    for i := 0; i < min(k - 1, n); i ++ {
        mx = max(mx, nums[i])
    }
    if n == 1 {
        if k % 2 == 1 {
            return -1
        } else {
            return nums[0]
        }
    } else {
        if k == 1 {
            return nums[1]
        } else {
            if n > k {
                return max(mx, nums[k])
            } else {
                return mx
            }
        }
    }
    return -1
}