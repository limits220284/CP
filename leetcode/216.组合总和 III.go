func combinationSum3(k int, n int) [][]int {
    ans := [][]int{}
    path := []int{}
    var dfs func(int, int)
    dfs = func(start, target int){
        if target == 0 {
            if len(path) == k {
                ans = append(ans, append([]int(nil), path...))
            }
            return
        }
        if target < 0 {
            return
        }
        for i := start; i <= 9; i++ {
            path = append(path, i)
            dfs(i + 1, target - i)
            path = path[:len(path) - 1]
        }       
    }
    dfs(1, n)
    return ans
}