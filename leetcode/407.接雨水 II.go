type cell struct{ h, x, y int }
type hp []cell
func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { return h[i].h < h[j].h }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(cell)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func max(a, b int) int {
    if b > a {
        return b
    }
    return a
}
func trapRainWater(heightMap [][]int) int {
    m, n := len(heightMap), len(heightMap[0])
    vis := make([][]bool, m)
    for i := range vis{
        vis[i] = make([]bool, n)
    }
    h := &hp{}
    for i, row := range heightMap{
        for j, v := range row{
            if i == 0 || i == m-1 || j == 0 || j == n-1{
                heap.Push(h, cell{v, i, j})
                vis[i][j] = true
            }
        }
    }
    ans := 0
    dirs := []int{-1, 0, 1, 0, -1}
    for h.Len() > 0{
        cur := heap.Pop(h).(cell)
        for k := 0; k < 4; k++{
            nx, ny := cur.x+dirs[k], cur.y+dirs[k+1]
            if 0 <= nx && nx < m && 0 <= ny && ny < n && !vis[nx][ny] {
                if heightMap[nx][ny] < cur.h {
                    ans += cur.h - heightMap[nx][ny]
                }
                vis[nx][ny] = true
                heap.Push(h, cell{max(heightMap[nx][ny], cur.h), nx, ny})
            }
        }
    }
    return ans
}
// # 采用的dijstra算法
//         m, n = len(heightMap), len(heightMap[0])
//         h = []
//         vis = [[False]*n for _ in range(m)]
//         # 将边缘点放进来
//         for i in range(m):
//             for j in range(n):
//                 if i == 0 or j == 0 or i == m-1 or j == n-1:
//                     vis[i][j] = True
//                     heappush(h, (heightMap[i][j], i, j))
//         inx = [0, 0, -1, 1]
//         iny = [1, -1, 0, 0]
//         ans = 0
//         while h:
//             # 每次弹出最小值
//             # 遍历该点周围的点
//             t, x, y = heappop(h)
//             for i in range(4):
//                 dx, dy = x + inx[i], y + iny[i]
//                 if 0 <= dx < m and 0 <= dy < n and not vis[dx][dy]:
//                     # 如果当前的点高度还小于该点，证明可以装下部分雨水，加入答案即可
//                     # 然后将该点加入到堆中
//                     if heightMap[dx][dy] <= t:
//                         ans += t - heightMap[dx][dy]
//                     heappush(h, (max(t, heightMap[dx][dy]), dx, dy))
//                     vis[dx][dy] = True
//         return ans