/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    x := root.Val
    if p.Val < x && q.Val < x {
        return lowestCommonAncestor(root.Left, p, q)
    }
    if p.Val > x && q.Val > x {
        return lowestCommonAncestor(root.Right, p, q)
    }
    return root
}