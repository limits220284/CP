/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func distributeCoins(root *TreeNode) int {
    // 什么b题目
    // 如果左边多余了，就上交，abs(数量)就是移动次数
    // 如果少了，就要，abs(数量)就是移动次数
    var dfs func(*TreeNode) int
    ans := 0
    dfs = func(root *TreeNode) int {
        if root == nil {
            return 0
        }
        l := dfs(root.Left)
        r := dfs(root.Right)
        ans += abs(l) + abs(r)
        d := l + r + root.Val - 1
        return d
    }
    dfs(root)
    return ans
}

func abs(x int) int {
    if x < 0 {
        x = -x
    }
    return x
}