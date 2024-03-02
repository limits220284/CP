func combinationSum2(candidates []int, target int) [][]int {
    ans := [][]int{}
    path := []int{}
    var dfs func(int, int)
    dfs = func(start, target int) {
        if target == 0 {
            temp := make([]int, len(path))
            copy(temp, path)
            ans = append(ans, temp)
            return
        }
        for i := start; i < len(candidates); i++ { //从start开始用来保证是组合
            if target - candidates[i] < 0 {
                break
            }
            if i > start && candidates[i] == candidates[i-1] { // 同一层如果有相同的，则表示
                continue
            }
            path = append(path, candidates[i])
            dfs(i + 1, target - candidates[i])
            path = path[: len(path) - 1]
        }
    }
    sort.Ints(candidates)
    dfs(0, target)
    return ans
}