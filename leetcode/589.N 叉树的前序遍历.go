/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func preorder(root *Node) []int {
    ans := make([]int, 0)
    var dfs func(_ *Node)
    dfs = func(root *Node) {
        if root == nil {
            return
        }
        ans = append(ans, root.Val)
        for _, node := range root.Children {
            dfs(node)
        }
    }
    dfs(root)
    return ans
}