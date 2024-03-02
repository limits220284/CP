func countPairs(d []int) int {
    // n := len(d)
    sort.Ints(d)
    mp := make(map[int]int)
    ans := 0
    MOD := int(1e9 + 7)
    for _, x := range d {
        for j := 0; j <= 22; j ++ {
            num := 1 << j
            if num < x {
                continue
            }
            if num - x > x {
                break
            }
            if val, ok := mp[num - x]; ok {
                ans += val
                ans %= MOD
                // fmt.Println(num, x)
            } 
        }
        mp[x] += 1
    }
    return ans % MOD
}