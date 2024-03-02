func generateParenthesis(n int) []string {
    var dfs func(int, int)
    ans := []string{}
    path := ""
    dfs = func(l, r int) {
        //左括号或者右括号
        if len(path) == 2 * n {
            if l == n && r == n {
                ans = append(ans, path)
            }
            return 
        }
        if r > l {
            return
        }
        //添加左括号
        path += "("
        dfs(l + 1, r)
        path = path[: len(path) - 1]
        path += ")"
        dfs(l, r + 1)
        path = path[: len(path) - 1]
    }
    dfs(0, 0)
    return ans
}