/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func longestZigZag(root *TreeNode) int {
    // 树形dp
    var dfs func(*TreeNode) (int, int)
    ans := 0
    dfs = func(root *TreeNode) (int, int) {
        if root == nil {
            return 0, 0
        }
        _, lr := dfs(root.Left)
        rl, _ := dfs(root.Right)
        ans = max(ans, max(lr, rl))
        return lr + 1, rl + 1
    }
    dfs(root)
    return ans
}
