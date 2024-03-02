func maxOperations(nums []int) int {
    n := len(nums)
    ans := 1
    prev := nums[0] + nums[1]
    for i := 2; i < n; i += 2 {
        if i >= n || i + 1 >= n {
            break
        }
        cur := nums[i] + nums[i + 1]
        if cur == prev {
            ans += 1
        } else {
            break
        }
    }
    return ans
}