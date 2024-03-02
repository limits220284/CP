func diagonalSum(mat [][]int) int {
    var n int = len(mat)
    var ans int = 0
    for i := 0; i < n; i++{
        ans += mat[i][i]
        ans += mat[i][n-1-i]
    }
    if n % 2 == 1{
        ans -= mat[n / 2][n / 2]
    }
    return ans
}