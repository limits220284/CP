/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    root := &ListNode{0, head}
    cur := head
    pre := root
    for cur != nil {
        if cur.Val == val {
            pre.Next = cur.Next
            cur = cur.Next
        } else {
            pre = pre.Next
            cur = cur.Next
        }
    }
    return root.Next
}