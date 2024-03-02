func numberOfBoomerangs(points [][]int) int {
    cnt := map[int]int{}
    ans := 0
    for _, p1 := range points {
        clear(cnt)
        for _, p2 := range points {
            d2 := (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1]-p2[1]) * (p1[1] - p2[1])
            ans += cnt[d2] * 2
            cnt[d2] += 1
        }
    }
    return ans
}
