func numberOfPairs(points [][]int) int {
    sort.Slice(points, func(i, j int) bool {
        return points[i][0] < points[j][0] || (points[i][0] == points[j][0] && points[i][1] > points[j][1])
    })
    n := len(points)
    // fmt.Println(points)
    ans := 0
    for i := 0; i < n; i ++ {
        up := math.MinInt
        for j := i + 1; j < n; j ++ {
            if points[j][1] > up && points[j][1] <= points[i][1]{
                up = points[j][1]
                ans += 1
            }
        }
    }
    return ans
}