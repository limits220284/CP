/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func countNodes(root *TreeNode) int {
    if root == nil {
        return 0
    }
    level := 0
    for node := root; node.Left != nil; node = node.Left {
        level += 1
    }
    return sort.Search(1 << (level + 1), func(k int) bool {
        if k <= 1 << level { // 如果小于k-1层，直接返回false即可
            return false
        }
        // k 如果小于等于四直接返回false
        // bits = 2
        // 如果k == 5， 101， 相当于最后一位是1，然后从左往右遍历
        // bits的位数就是移动的次数
        // 如果是6，怎么操作呢
        // 110, 相当于最高位是1，然后从高往低遍历，看怎么走即可
        bits := 1 << (level - 1) // 2
        node := root
        for node != nil && bits > 0 {
            if bits & k == 0 {
                node = node.Left
            } else {
                node = node.Right
            }
            bits >>= 1
        }
        return node == nil
    }) - 1
}
