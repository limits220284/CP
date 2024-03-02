/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal(root *TreeNode) (vals []int) {
    stk := []*TreeNode{}
    node := root
    for node != nil || len(stk) > 0 {
        for node != nil {
            vals = append(vals, node.Val)
            stk = append(stk, node)
            node = node.Left
        }
        node = stk[len(stk) - 1].Right
        stk = stk[:len(stk) - 1]
    }
    return
}