const mx int = 1e5 + 1
var np = [mx]bool{1: true}
func init() {
    for i := 2; i * i < mx; i ++ {
        if !np[i] {
            for j := i * i; j < mx; j += i {
                np[j] = true
            }
        }
    }
}
// 以每一个质数为节点，然后dfs一下与其连接的所有非质数节点，然后进行结果统计即可
func countPaths(n int, edges [][]int) int64 {
    g := make([][]int, n + 1)
    for _, e := range edges {
        x, y := e[0], e[1]
        g[x] = append(g[x], y)
        g[y] = append(g[y], x)
    }
    size := make([]int, n + 1)
    var nodes []int
    var dfs func(int, int)
    dfs = func(x, fa int) {
        nodes = append(nodes, x)
        for _, y := range g[x] {
            if y != fa && np[y] {
                dfs(y, x)
            }
        }
    }
    ans := 0
    for x := 1; x <= n; x ++ {
        if np[x] {
            continue
        }
        sum := 0
        for _, y := range g[x] {
            if !np[y] {
                continue
            }
            if size[y] == 0 {
                nodes = []int{}
                dfs(y, -1)
                for _, z := range nodes {
                    size[z] = len(nodes)
                }
            }
            ans += size[y] * sum
            sum += size[y]
        }
        ans += sum
    }
    return int64(ans)
}