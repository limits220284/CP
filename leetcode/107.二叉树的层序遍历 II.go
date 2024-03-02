/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrderBottom(root *TreeNode) [][]int {
    if root == nil {
        return [][]int{}
    }
    ans := [][]int{}
    q := []*TreeNode{root}
    for len(q) > 0 {
        vals := []int{}
        n := len(q)
        for i := 0; i < n; i++ {
            node := q[0]
            q = q[1:]
            vals = append(vals, node.Val)
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        ans = append(ans, vals)
    }
    for i := 0; i < len(ans) / 2; i++ {
        ans[i], ans[len(ans) - 1 - i] = ans[len(ans) - 1 - i], ans[i]
    }
    return ans
}