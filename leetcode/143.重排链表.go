/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//链表中点
func FindMiddleNode(head *ListNode) *ListNode{
    slow, fast := head, head
    for fast != nil && fast.Next != nil{
        slow = slow.Next
        fast = fast.Next.Next
    }
    return slow
}
//反转链表
func reverseListNode(head *ListNode) *ListNode{
    var pre, cur *ListNode = nil, head
    for cur != nil {
        temp := cur.Next
        cur.Next = pre
        pre = cur
        cur = temp
    }
    return pre
}
func reorderList(head *ListNode)  {
    mid := FindMiddleNode(head)
    head2 := reverseListNode(mid)
    for head2.Next != nil{
        t1 := head.Next
        t2 := head2.Next
        head.Next = head2
        head2.Next = t1
        head = t1
        head2 = t2
    }
}
