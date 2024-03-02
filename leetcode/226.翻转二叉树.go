/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    q := []*TreeNode{root}
	for len(q) > 0 {
		t := q[0]
		q = q[1:]
		t.Left, t.Right = t.Right, t.Left
		if t.Left != nil {
			q = append(q, t.Left)
		}
		if t.Right != nil {
			q = append(q, t.Right)
		}
	}
	return root
}