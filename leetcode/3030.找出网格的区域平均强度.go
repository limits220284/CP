func resultGrid(a [][]int, threshold int) [][]int {
    m, n := len(a), len(a[0])
    result := make([][]int, m)
    cnt := make([][]int, m)
    for i := range result {
        result[i] = make([]int, n)
        cnt[i] = make([]int, n)
    }
    for i := 2; i < m; i ++ {
    next:
        for j := 2; j < n; j ++ {
            // 检查左右相邻格子
            for _, row := range a[i - 2: i + 1] {
                if abs(row[j - 2] - row[j - 1]) > threshold || abs(row[j - 1] - row[j]) > threshold {
                    continue next
                }
            }
            // 检查上下相邻格子
            for y := j - 2; y <= j; y ++ {
                if abs(a[i-2][y]-a[i-1][y]) > threshold || abs(a[i-1][y]-a[i][y]) > threshold {
					continue next // 不合法，下一个
				}
            }
            
            // 合法，计算 3 X 3网格的平均值
            avg := 0
            for x := i - 2; x <= i; x ++ {
                for y := j - 2; y <= j; y ++ {
                    avg += a[x][y]
                }
            }
            avg /= 9
            
            // 更新3x3子网格内的result
            for x := i - 2; x <= i; x ++ {
                for y := j - 2; y <= j; y ++ {
                    result[x][y] += avg
                    cnt[x][y] += 1
                }
            }
        }
    }
    for i, row := range cnt {
        for j, c := range row {
            if c == 0 {
                result[i][j] = a[i][j]
            } else {
                result[i][j] /= c
            }
        }
    }
    return result
}
func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}