func maxArea(height []int) int {
    //注意为什么能够使用双指针解法
    n := len(height)
    l, r := 0, n-1
    ans := 0
    for l < r {
        ans = max(ans, (r - l) * min(height[r], height[l]))
        if height[l] < height[r] {
            l += 1
        }else{
            r -= 1
        }
    }
    return ans
}
func min(a, b int) int{
    if a < b {
        return a
    }
    return b
}
func max(a, b int) int{
    if a < b {
        return b
    }
    return a
}