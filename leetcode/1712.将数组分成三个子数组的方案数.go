func waysToSplit(nums []int) int {
    MOD := int(1e9 + 7)
    n := len(nums)
    s := make([]int, n + 1)
    for i, x := range nums {
        s[i + 1] = s[i] + x
    }
    ans := 0
    for i := 0; i < n - 2; i ++ {
        left := s[i + 1]
        l, r := i + 1, n - 2
        for l < r {
            mid := (l + r) / 2
            if s[mid + 1] - s[i + 1] >= left {
                r = mid
            } else {
                l = mid + 1
            }
        }
        if s[l + 1] - s[i + 1] < left {
            continue
        }
        ll := l
        l, r = i + 1, n - 2
        for l < r {
            mid := (l + r + 1) / 2
            if s[mid + 1] - s[i + 1] <= s[n] - s[mid + 1] {
                l = mid
            } else {
                r = mid - 1
            }
        }
        if s[l + 1] - s[i + 1] > s[n] - s[l + 1] {
            continue
        }
        rr := l
        if ll > rr {
            continue
        }
        ans += rr - ll + 1
        ans %= MOD
    }
    return ans % MOD
}