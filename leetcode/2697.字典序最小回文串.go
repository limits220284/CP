func makeSmallestPalindrome(s string) string {
    l, r := 0, len(s) - 1
    t := []byte(s)
    for l < r {
        if s[l] != s[r] {
            t[l] = min(s[l], s[r])
            t[r] = t[l]
        }
        l += 1
        r -= 1
    }
    return string(t)
}