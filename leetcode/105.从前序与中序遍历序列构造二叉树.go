/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0 {
        return nil
    }
    root := &TreeNode{Val: preorder[0]}
    // 确定根节点的位置
    idx := 0
    for i, val := range inorder {
        if val == preorder[0] {
            idx = i
            break
        }
    }
    root.Left = buildTree(preorder[1: idx + 1], inorder[: idx])
    root.Right = buildTree(preorder[idx + 1:], inorder[idx + 1:])
    return root
}