func longestCycle(edges []int) int {
    // 拓扑排序找到所有的环，然后深度优先搜索遍历每一个环即可
    time := make([]int, len(edges))
    clock, ans := 1, -1
    n := len(edges)
    for i := 0; i < n; i++ {
        if time[i] > 0 {
            continue
        }
        startTime := clock
        x := i
        for x != -1 {
            // 找到了一个访问过的点
            if time[x] > 0 {
                if time[x] >= startTime {
                    ans = max(ans, clock - time[x])
                }
                break
            }
            time[x] = clock
            clock += 1
            x = edges[x]
        }
    }
    return ans
}