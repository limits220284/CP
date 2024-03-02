/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deepestLeavesSum(root *TreeNode) int {
    //广度优先搜索
    ans := 0
    q := []*TreeNode{root}
    for len(q) > 0 {
        m := len(q)
        tmp := 0
        for i := 0; i < m; i++ {
            t := q[0]
            q = q[1:]
            tmp += t.Val
            if t.Left != nil {
                q = append(q, t.Left)
            }
            if t.Right != nil {
                q = append(q, t.Right)
            }
        }
        ans = tmp
    }
    return ans
}