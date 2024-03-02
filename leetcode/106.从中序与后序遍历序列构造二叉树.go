/*
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
*/

func buildTree(inorder []int, postorder []int) *TreeNode {
    // if inorder == nil {
    //     return nil
    // }
    n := len(inorder)
    if n == 0 {
        return nil
    }
    root := &TreeNode{Val: postorder[n - 1]}
    idx := 0 
    for i, val := range inorder {
        if val == postorder[n - 1] {
            idx = i
            break
        }
    }
    
    root.Left = buildTree(inorder[:idx], postorder[:idx])
    root.Right = buildTree(inorder[idx + 1:], postorder[idx: n - 1])
    return root
}