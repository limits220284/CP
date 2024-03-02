/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) [][]int {
    ans := [][]int{}
    var dfs func(*TreeNode, int)
    path := []int{}
    dfs = func(node *TreeNode, target int) {
        if node == nil {
            return
        }
        target -= node.Val
        path = append(path, node.Val)
        if node.Left == nil && node.Right == nil && target == 0{
            ans = append(ans, append([]int(nil), path...))
        }
        dfs(node.Left, target)
        dfs(node.Right, target)
        path = path[:len(path)-1]
    }
    dfs(root, targetSum)
    return ans
}