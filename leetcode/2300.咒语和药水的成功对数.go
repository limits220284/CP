func successfulPairs(spells []int, potions []int, success int64) []int {
    sort.Ints(potions)
    n := len(potions)
    ans := []int{}
    for _, x := range(spells) {
        l, r := 0, n - 1
        for l < r {
            mid := (l + r) / 2
            if int64(potions[mid] * x) >= success {
                r = mid
            } else {
                l = mid + 1
            }
        }
        if int64(potions[l] * x) >= success {
            ans = append(ans, n - l)
        } else {
            ans = append(ans, 0)
        }
        
    } 
    return ans
}