/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func binaryTreePaths(root *TreeNode) []string {
    paths := []string{}
    var dfs func(_ *TreeNode, path string)
    dfs = func(root *TreeNode, path string) {
        if root == nil {
            return
        }
        path += strconv.Itoa(root.Val)
        if root.Left == nil && root.Right == nil {
            paths = append(paths, path)
            return
        }
        path += "->"
        dfs(root.Left, path)
        dfs(root.Right, path)
    }
    dfs(root, "")
    return paths
}