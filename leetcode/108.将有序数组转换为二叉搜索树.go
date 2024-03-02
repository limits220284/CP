/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    n := len(nums)
    var dfs func(l, r int) *TreeNode
    dfs = func(l, r int) *TreeNode {
        mid := (l + r) / 2
        if l > r {
            return nil
        }
        root := &TreeNode{Val: nums[mid]}
        root.Left = dfs(l, mid - 1)
        root.Right = dfs(mid + 1, r)
        return root
    }
    return dfs(0, n - 1)
}