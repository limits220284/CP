/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func dfs(node *TreeNode) (int, *TreeNode) {
    if node == nil {
        return 0, nil
    }
    leftHeight, leftLCA := dfs(node.Left)
    rightHeight, rightLCA := dfs(node.Right)
    if leftHeight > rightHeight { // 左子树更高
        return leftHeight + 1, leftLCA
    }
    if leftHeight < rightHeight { // 右子树更高
        return rightHeight + 1, rightLCA
    }
    return leftHeight + 1, node // 一样高
}
func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
    _, lca := dfs(root)
    return lca
}