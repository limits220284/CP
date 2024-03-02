func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
    postMap := map[int]int{}
    for i, v := range postorder {
        postMap[v] = i
    }
    var dfs func(int, int, int, int) *TreeNode
    dfs = func (preLeft, preRight, postLeft, postRight int) *TreeNode {
        if preLeft > preRight {
            return nil
        }
        leftCount := 0
        if preLeft < preRight {
            leftCount = postMap[preorder[preLeft + 1]] - postLeft + 1
        }
        return &TreeNode{
            Val: preorder[preLeft],
            Left: dfs(preLeft + 1, preLeft + leftCount, postLeft, postLeft + leftCount - 1),
            Right: dfs(preLeft + leftCount + 1, preRight, postLeft + leftCount, postRight - 1),
        }
    }
    return dfs(0, len(preorder) - 1, 0, len(postorder) - 1)
}