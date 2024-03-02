/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNodes(head *ListNode) *ListNode {
    var st []*ListNode
    for ; head != nil; head = head.Next {
        st = append(st, head)
    }
    for ; len(st) > 0; st = st[: len(st) - 1] {
        if head == nil || st[len(st) - 1].Val >= head.Val {
            st[len(st) - 1].Next = head
            head = st[len(st) - 1]
        }
    }
    return head
}