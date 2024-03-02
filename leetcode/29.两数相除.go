func divide(dividend int, divisor int) int {
    // 真nm惯着你了
    ans := dividend / divisor
    if ans > 1 << 31 - 1 {
        ans = 1 << 31 - 1
    }
    return ans
}