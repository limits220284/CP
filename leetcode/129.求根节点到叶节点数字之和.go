/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumNumbers(root *TreeNode) int {
    ans := 0
    var dfs func(*TreeNode, int)
    dfs = func(node *TreeNode, tot int) {
        if node == nil {
            return 
        }
        tot = tot * 10 + node.Val
        if node.Left == nil && node.Right == nil {
            ans += tot
        }
        dfs(node.Left, tot)
        dfs(node.Right, tot)
        // tot /= 10
    }
    dfs(root, 0)
    return ans
}