/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    //维护左子树和右子树之间的高度差
    var dfs func(node *TreeNode) int
    ans := true
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        l := dfs(node.Left)
        r := dfs(node.Right)
        if abs(r - l) > 1 {
            ans = false
        }
        return max(l, r) + 1
    }
    dfs(root)
    return ans
}
func abs(x int) int{
    if x < 0 {
        return -x
    }
    return x
}