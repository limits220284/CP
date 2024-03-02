/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
	if root == nil {
        return root
    }
    q := []*Node{root}
    for len(q) > 0 {
        m := len(q)
        for i := 0; i < m; i++ {
            node := q[0]
            if i + 1 < m {
                node.Next = q[1]
            }
            q = q[1:]
            if node.Left != nil{
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
    }
    return root
}