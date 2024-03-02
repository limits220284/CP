/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pseudoPalindromicPaths (root *TreeNode) int {
    // 如果是伪回文的，那么数字出现奇数的数量只能小于等于1
    cnt := make([]int, 9)
    var dfs func(*TreeNode)
    ans := 0
    dfs = func(root *TreeNode) {
        if root == nil {
            return
        }
        cnt[root.Val - 1] += 1
        if root.Left == root.Right {
            t := 0
            for _, x := range cnt {
                if x % 2 == 1 {
                    t += 1
                }
            }
            if t <= 1 {
                ans += 1
            }
        }
        dfs(root.Left)
        dfs(root.Right)
        cnt[root.Val - 1] -= 1
    }
    dfs(root)
    return ans
}