func findTheLongestBalancedSubstring(s string) int {
    pre, cur := 0, 0
    ans := 0
    for i, c := range s {
        cur += 1
        if i == len(s) - 1 || byte(c) != s[i + 1] {
            if c == '1' {
                ans = max(ans, min(pre, cur) * 2)
            }
            pre = cur
            cur = 0
        }
    }
    return ans
}