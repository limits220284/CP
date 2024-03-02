func minimumTimeToInitialState(s string, k int) int {
    n := len(s)
    for i := k; i < n; i += k {
        if strings.HasPrefix(s, s[i:]) {
            return i / k
        }
    }
    return (n - 1) / k + 1
}