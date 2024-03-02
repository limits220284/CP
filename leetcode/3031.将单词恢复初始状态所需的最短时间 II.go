func minimumTimeToInitialState(s string, k int) int {
    n := len(s)
    for i := k; i < n; i += k {
        if strings.HasPrefix(s, s[i:]) {
            return i / k
        }
    }
    return int(math.Ceil(float64(n) / float64(k)))
}