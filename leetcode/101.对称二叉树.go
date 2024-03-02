/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    var dfs func(p, q *TreeNode) bool
    dfs = func(p, q *TreeNode) bool {
        if p == nil && q == nil {
            return true
        }
        if p == nil || q == nil {
            return false
        }
        if p.Val != q.Val {
            return false
        }
        return dfs(p.Right, q.Left) && dfs(p.Left, q.Right)
    }
    return dfs(root.Left, root.Right)
}