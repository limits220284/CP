/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    ans := []*TreeNode{}
    cnt := map[int]bool{}
    for _, x := range(to_delete) {
        cnt[x] = true
    }
    var dfs func(node *TreeNode) *TreeNode
    dfs = func(node *TreeNode) *TreeNode {
        if node == nil {
            return nil
        }
        node.Left = dfs(node.Left)
        node.Right = dfs(node.Right)
        if cnt[node.Val] == false {
            return node
        }
        if node.Left != nil {
            ans = append(ans, node.Left)
        }
        if node.Right != nil {
            ans = append(ans, node.Right)
        }
        return nil
    }
    if dfs(root) != nil {
        ans = append(ans, root)
    }
    return ans
}