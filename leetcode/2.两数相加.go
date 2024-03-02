/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    flag := 0
    dummy := &ListNode{0, nil}
    cur := dummy
    for l1 != nil && l2 != nil {
        val := (l1.Val + l2.Val + flag) % 10
        flag = (l1.Val + l2.Val + flag) / 10
        cur.Next = &ListNode{val, nil}
        cur = cur.Next
        l1, l2 = l1.Next, l2.Next
    }
    for l1 != nil {
        val := (l1.Val + flag) % 10
        flag = (l1.Val + flag) / 10
        cur.Next = &ListNode{val, nil}
        cur = cur.Next
        l1 = l1.Next
    }
    for l2 != nil {
        val := (l2.Val + flag) % 10
        flag = (l2.Val + flag) / 10
        cur.Next = &ListNode{val, nil}
        cur = cur.Next
        l2 = l2.Next
    }
    if flag == 1 {
        cur.Next = &ListNode{1, nil}
    }
    return dummy.Next
}