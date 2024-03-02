func rootCount(edges [][]int, guesses [][]int, k int) int {
    // 换根dp
    // 每次先用某一个当成根节点，计算出当前结果
    // 然后换成子节点
    // 需要先dfs一次，找到以0为根节点的满足guess的个数
    // 然后换根dp，求出每一次的结果，最后进行统计就行
    n := len(edges) + 1
    g := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        g[a] = append(g[a], b)
        g[b] = append(g[b], a)
    }
    type pair struct {x, y int}
    hsh := make(map[pair]int)
    for _, gue := range guesses {
        hsh[pair{gue[0], gue[1]}] = 1
    }
    var dfs func(int, int)
    gus0 := 0
    dfs = func(x, fa int) {
        for _, y := range g[x] {
            if y == fa {
                continue
            }
            if _, ok := hsh[pair{x, y}]; ok {
                gus0 += 1
            }
            dfs(y, x)
        }
    }
    dfs(0, -1)
    ans := 0
    var reroot func(int, int, int)
    reroot = func(x, fa, cnt int) {
        if cnt >= k {
            ans += 1
        }
        for _, y := range g[x] {
            if y != fa {
                reroot(y, x, cnt - hsh[pair{x, y}] + hsh[pair{y, x}])
            }
        }
    }
    reroot(0, -1, gus0)
    return ans
}