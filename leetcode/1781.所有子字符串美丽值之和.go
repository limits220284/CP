func beautySum(s string) int {
    n := len(s)
    ans := 0
    for i := 0; i < n; i++ {
        mp := [26]int{}
        for j := i; j < n; j++ {
            mx := 0
            mi := n
            mp[s[j] - 'a'] += 1
            for _, x := range mp {
                if x != 0 {
                    mx = max(mx, x)
                    mi = min(mi, x)
                }
            }
            ans += mx - mi
        }
    }
    return ans
}