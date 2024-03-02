/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDepth(root *TreeNode) int {
    if root == nil{
        return 0
    }
    if root.Left == nil && root.Right == nil {
        return 1
    }
    l, r := math.MaxInt, math.MaxInt
    if root.Left != nil {
        l = min(l, minDepth(root.Left))
    }
    if root.Right != nil {
        r = min(r, minDepth(root.Right))
    }
    return min(l, r) + 1
}