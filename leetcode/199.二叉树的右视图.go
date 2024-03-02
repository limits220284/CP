/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    ans := []int{}
    q := []*TreeNode{root}
    for len(q) > 0 {
        m := len(q)
        vals := []int{}
        for i := 0; i < m; i++ {
            t := q[0]
            q = q[1:]
            vals = append(vals, t.Val)
            if t.Left != nil {
                q = append(q, t.Left)
            }
            if t.Right != nil {
                q = append(q, t.Right)
            }
        }
        ans = append(ans, vals[len(vals) - 1])
    }
    return ans
}