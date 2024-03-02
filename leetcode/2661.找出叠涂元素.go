func firstCompleteIndex(arr []int, mat [][]int) int {
    m, n := len(mat), len(mat[0])
    cnt := make(map[int][2]int)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            cnt[mat[i][j]] = [2]int{i, j}
        }
    }
    col := make([]int, n)
    row := make([]int, m)
    ans := 0
    for i, c := range(arr) {
        x, y := cnt[c][0], cnt[c][1]
        col[y] += 1
        row[x] += 1
        if col[y] == m || row[x] == n {
            ans = i
            break
        }
    }
    return ans
}