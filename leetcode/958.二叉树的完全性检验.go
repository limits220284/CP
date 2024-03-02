/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type Node struct  {
    node *TreeNode
    val int
}
func isCompleteTree(root *TreeNode) bool {
    //bfs检验是否是完全二叉树
    nodes := []Node{Node{root, 1}}
    i := 0
    for i < len(nodes) {
        node, v := nodes[i].node, nodes[i].val
        i += 1
        if node != nil {
            nodes = append(nodes, Node{node.Left, 2 * v})
            nodes = append(nodes, Node{node.Right, 2 * v + 1})
        }
    }
    fmt.Print(nodes)
    return nodes[len(nodes) - 1].val == len(nodes)
}