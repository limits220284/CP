/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    var dfs func(_ * TreeNode) (int, int)
    res := true
    dfs = func(node *TreeNode) (int, int) {
        if node == nil {
            return math.MaxInt, math.MinInt
        }
        lmi, lmx := dfs(node.Left)
        rmi, rmx := dfs(node.Right)
        if lmx >= node.Val || rmi <= node.Val {
            res = false
        }
        return min(node.Val, min(lmi, rmi)), max(node.Val, max(lmx, rmx))
    }
    dfs(root)
    return res
}