func maxCompatibilitySum(students [][]int, mentors [][]int) int {
    // 直接暴力回溯即可
    var dfs func(int, int)
    n := len(students)
    m := len(students[0])
    vis := make([]bool, n)
    ans := 0
    dfs = func(start, res int) {
        if start == n {
            ans = max(ans, res)
            return
        }
        // 枚举选哪个
        for i := 0; i < n; i++ {
            if vis[i] == true {
                continue
            }
            vis[i] = true
            tp := 0
            for j := 0; j < m; j++ {
                if students[start][j] == mentors[i][j] {
                    tp += 1
                }
            }
            dfs(start + 1, res + tp)
            vis[i] = false
        }
    } 
    dfs(0, 0)
    return ans
}