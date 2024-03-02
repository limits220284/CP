/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxAncestorDiff(root *TreeNode) int {
    //维护子树的最大值和最小值即可
    var dfs func(*TreeNode) (int, int)
    ans := 0
    dfs = func(node *TreeNode) (int, int){
        if node == nil {
            // fmt.Println(math.MaxInt, math.MinInt)
            return math.MaxInt / 2, math.MinInt / 2
        }
        lmi, lmx := dfs(node.Left)
        rmi, rmx := dfs(node.Right)
        ans = max(ans, node.Val - lmi)
        ans = max(ans, node.Val - rmi)
        ans = max(ans, -node.Val + lmx)
        ans = max(ans, -node.Val + rmx)
        // fmt.Println(ans)
        // fmt.Println(min(node.Val, min(lmi, rmi)), max(node.Val, max(lmx, rmx)))
        return min(node.Val, min(lmi, rmi)), max(node.Val, max(lmx, rmx))
    }
    dfs(root)
    return ans
}
func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}