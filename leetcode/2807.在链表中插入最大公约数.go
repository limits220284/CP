/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    node := head
    for node.Next != nil {
        node.Next = &ListNode{gcd(node.Val, node.Next.Val), node.Next}
        node = node.Next.Next
    }
    return head
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a % b
    }
    return a
}