/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(node *Node) *Node {
    //层序遍历 + 链表
    root := node
    for root != nil {
        dummy := &Node{}
        cur := dummy
        for root != nil {
            if root.Left != nil {
                cur.Next = root.Left
                cur = cur.Next
            }
            if root.Right != nil {
                cur.Next = root.Right
                cur = cur.Next
            }
            root = root.Next
        }
        root = dummy.Next
    }
    return node
}