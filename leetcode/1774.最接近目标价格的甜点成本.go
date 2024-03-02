func closestCost(baseCosts []int, toppingCosts []int, target int) int {
    for _, x := range(toppingCosts) {
        toppingCosts = append(toppingCosts, x)
    }
    sort.Ints(toppingCosts)
    n := len(toppingCosts)
    var dfs func(int, int)
    ans := math.MaxInt
    diff := math.MaxInt
    dfs = func(start, tot int) {
        if abs(tot - target) <= diff {
            if abs(tot - target) == diff {
                ans = min(ans, tot)
            } else{
                ans = tot
            }
            diff = abs(tot - target)
        }
        for i := start; i < n; i++ {
            // if i > start && toppingCosts[i] == toppingCosts[i-1] {
            //     continue
            // }
            dfs(i + 1, tot + toppingCosts[i])
        }
    }
    for _, x := range(baseCosts) {
        dfs(0, x)
    }
    return ans
}
func abs(x int) int{
    if x < 0 {
        return -x
    }
    return x
}