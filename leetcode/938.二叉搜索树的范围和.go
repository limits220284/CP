/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, low int, high int) int {
    // 中序遍历是单调递增的
    var dfs func(*TreeNode)
    ans := 0
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        dfs(node.Left)
        if node.Val >= low && node.Val <= high {
            ans += node.Val
        }
        dfs(node.Right)
    }
    dfs(root)
    return ans
}