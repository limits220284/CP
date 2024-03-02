func closestMeetingNode(edges []int, node1 int, node2 int) int {
    // 图中最近公共祖先问题
    n := len(edges)
    calcDis := func(x int) []int {
        dis := make([]int, n)
        for i := range dis {
            dis[i] = n
        }
        for d := 0; x >= 0 && dis[x] == n; x = edges[x] {
            dis[x] = d
            d += 1
        }
        return dis
    }
    d1 := calcDis(node1)
    d2 := calcDis(node2)
    minDis, ans := n, -1
    for i, d := range d1 {
        if d2[i] > d {
            d = d2[i]
        }
        if d < minDis {
            minDis, ans = d, i
        }
    }
    return ans
}