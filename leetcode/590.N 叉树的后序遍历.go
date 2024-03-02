/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func postorder(root *Node) []int {
    var dfs func(*Node)
    ans := []int{}
    dfs = func(node *Node) {
        if node == nil {
            return
        }
        for _, child := range node.Children {
            dfs(child)
        }
        ans = append(ans, node.Val)
    }
    dfs(root)
    return ans
}