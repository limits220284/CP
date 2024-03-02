func addMinimum(s string) int {
    ans := int(s[0]) - int(s[len(s) - 1]) + 2
    for i := 1; i < len(s); i ++ {
        ans += (int(s[i]) - int(s[i - 1]) + 2) % 3
    }
    return ans
}