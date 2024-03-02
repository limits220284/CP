/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxLevelSum(root *TreeNode) int {
    mx := math.MinInt
    idx := -1
    step := 1
    q := []*TreeNode{root}
    for len(q) > 0 {
        tot := 0
        m := len(q)
        for i := 0; i < m; i++ {
            t := q[0]
            tot += t.Val
            q = q[1:]
            if t.Left != nil {
                q = append(q, t.Left)
            }
            if t.Right != nil {
                q = append(q, t.Right)
            }
        }
        if tot > mx {
            mx = tot
            idx = step
        }
        step += 1
    }
    return idx
}