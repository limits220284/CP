func combinationSum(candidates []int, target int) [][]int {
    ans := [][]int{}
    path := []int{}
    var dfs func(int, int)
    dfs = func(start, target int) {
        //选或者不选
        //枚举选哪个
        if target == 0 {
            temp := make([]int, len(path))
            copy(temp, path)
            ans = append(ans, temp)
            return
        }
        for i := start; i < len(candidates); i++ {
            if target - candidates[i] < 0 {
                break
            }
            path = append(path, candidates[i])
            dfs(i, target - candidates[i])
            path = path[: len(path) - 1]
        }
    }
    sort.Ints(candidates)
    dfs(0, target)
    return ans
}