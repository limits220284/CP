func maxTaxiEarnings(n int, rides [][]int) int64 {
    sort.Slice(rides, func(i, j int) bool {
        return rides[i][1] < rides[i][0]
    })
    f := make([]int64, n + 1)
    dic := map[int][][]int{}
    for _, ride := range rides {
        dic[ride[1]] = append(dic[ride[1]], []int{ride[0], ride[2]})
    }
    for i := 1; i <= n; i++ {
        f[i] = max(f[i], f[i - 1])
        for _, ride := range dic[i] {
            f[i] = max(f[i], f[ride[0]] + int64(i - ride[0] + ride[1]))
        }
    }
    return f[n]
}