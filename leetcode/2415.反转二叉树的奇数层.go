/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func swap(a, b *TreeNode) {
    a.Val, b.Val = b.Val, a.Val
}

func reverseOddLevels(root *TreeNode) *TreeNode {
    q := []*TreeNode{root}
    step := 0
    for len(q) > 0 {
        m := len(q)
        if step % 2 == 1 {
            for i := 0; i < m / 2; i++ {
                swap(q[i], q[m - 1 - i])
            }
        }
        for i := 0; i < m; i++ {
            t := q[0]
            q = q[1:]
            if t.Left != nil {
                q = append(q, t.Left)
            }
            if t.Right != nil {
                q = append(q, t.Right)
            }
        }
        step += 1
    }
    return root
}