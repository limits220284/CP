func queryString1(s string, n int) bool {
    N := len(s)
    mp := make(map[int]bool)
    for i := 0; i < N; i ++ {
        if s[i] == '0' {
            continue
        }
        t := 0
        for j := i; j < N; j ++ {
            t = t * 2 + int(s[j] - '0')
            if t > n {
                break
            }
            mp[t] = true
        }
    }
    return len(mp) == n
}

func queryString(s string, n int) bool {
    for i := 1; i <= n; i ++ {
        if !strings.Contains(s, strconv.FormatUint(uint64(i), 2)) {
            return false
        }
    }
    return true
}

