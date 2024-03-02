/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func bstToGst(root *TreeNode) *TreeNode {
    var dfs func(*TreeNode)
    mx := 0
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        dfs(node.Right)
        mx += node.Val
        node.Val = mx
        dfs(node.Left)
    }
    dfs(root)
    return root
}