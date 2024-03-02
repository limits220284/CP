/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargestLevelSum(root *TreeNode, k int) int64 {
    q := []*TreeNode{root}
    ans := []int{}
    for len(q) > 0 {
        n := len(q)
        tot := 0
        for i := 0; i < n; i ++ {
            node := q[0]
            tot += node.Val
            q = q[1:]
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        ans = append(ans, tot)
    }
    if len(ans) < k {
        return -1
    }
    sort.Slice(ans, func(i, j int) bool {
        return ans[i] >= ans[j]
    })
    return int64(ans[k - 1])
}