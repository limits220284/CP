/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    //需要定义三个节点，pre, cur, nxt
    if head == nil {
        return nil
    }
    root := &ListNode{0, head}
    pre := root
    cur := head
    for cur != nil && cur.Next != nil {
        nxt := cur.Next
        if cur.Val == nxt.Val {
            for nxt != nil && cur.Val == nxt.Val {
                cur.Next = nxt.Next
                nxt = nxt.Next
            }
            pre.Next = nxt
            cur = nxt
        } else {
            pre = cur
            cur = cur.Next
        }
    }
    return root.Next
}