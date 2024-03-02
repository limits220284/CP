func returnToBoundaryCount(nums []int) int {
    ans := 0
    idx := 0
    for _, x := range nums {
        idx += x
        if idx == 0 {
            ans += 1
        }
    }
    return ans
}