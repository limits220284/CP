/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func amountOfTime(root *TreeNode, start int) int {
    // 记录根节点到当前点的距离，然后记录另外一条边的最长的距离，取最大值即可
    var dfs func(*TreeNode) (int, bool)
    mx := 0
    start_root := 0
    dfs = func(root *TreeNode) (int, bool) {
        if root == nil {
            return -1, false
        }
        lh, fl := dfs(root.Left)
        rh, fr := dfs(root.Right)
        if root.Val == start {
            mx = max(mx, max(lh, rh) + 1)
            start_root = 0
        }
        if fl {
            start_root += 1
            mx = max(mx, rh + 1 + start_root)
        }
        if fr {
            start_root += 1
            mx = max(mx, lh + 1 + start_root)
        }
        return max(lh, rh) + 1, fl || fr || root.Val == start
    }
    dfs(root)
    return mx
}