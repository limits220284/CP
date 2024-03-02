func colorTheArray(n int, queries [][]int) []int {
    m := len(queries)
    if n == 1 {
        return make([]int, m)
    }
    //直接模拟即可
    f := make([]int, n)
    ans := []int{}
    cnt := 0
    for i := 0; i < m; i++ {
        idx, val := queries[i][0], queries[i][1]
        if idx > 0 && f[idx - 1] > 0 {
            if f[idx] == f[idx - 1] {
                cnt -= 1
            }
            if val == f[idx - 1] {
                cnt += 1
            }
        } 
        if idx < n - 1 && f[idx + 1] > 0 {
            if f[idx] == f[idx + 1] {
                cnt -= 1
            }
            if f[idx + 1] == val {
                cnt += 1
            }
        }
        f[idx] = val
        ans = append(ans, cnt)
    }
    return ans
}