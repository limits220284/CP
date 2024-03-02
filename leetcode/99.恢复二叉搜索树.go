/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func recoverTree(root *TreeNode)  {
    //直接中序遍历即可
    //需要两次中序遍历
    pre := &TreeNode{Val:math.MinInt}
    var target1 *TreeNode
    var target2 *TreeNode
    var dfs func(_ *TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return 
        }
        dfs(node.Left)
        if node.Val <= pre.Val {
            if pre.Val >= node.Val {
                if target1 == nil {
                    target1 = pre
                    target2 = node
                }else{
                    target2 = node
                    return
                }
            }
        }
        pre = node
        dfs(node.Right)
    }
    dfs(root)
    target1.Val, target2.Val = target2.Val, target1.Val
}