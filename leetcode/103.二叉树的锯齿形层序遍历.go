/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
    ans := [][]int{}
    if root == nil {
        return ans
    }
    q := []*TreeNode{root}
    for even := false; len(q) > 0; even = !even {
        n := len(q)
        vals := make([]int, n)
        for i := 0; i < n; i++ {
            t := q[0]
            q = q[1:]
            if even {
                vals[n - 1 - i] = t.Val
            } else {
                vals[i] = t.Val
            }
            if t.Left != nil {
                q = append(q, t.Left)
            }
            if t.Right != nil {
                q = append(q, t.Right)
            }
        }
        ans = append(ans, vals)
    }
    return ans
}