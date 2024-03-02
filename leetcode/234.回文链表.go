/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    // 定义一个头节点，然后采用三个指针反转链表
    if head == nil {
        return nil
    }
    var pre *ListNode
    cur := head
    for cur != nil {
        nxt := cur.Next
        cur.Next = pre
        pre = cur
        cur = nxt
    }
    return pre
}

func endOfFirstHalf(head *ListNode) *ListNode {
    fast := head
    slow := head
    for fast.Next != nil && fast.Next.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
    }
    return slow
}

func isPalindrome(head *ListNode) bool {
    // 快慢指针找到中间节点
    if head == nil {
        return true
    }
    firstHalfEnd := endOfFirstHalf(head)
    secondHalfStart := reverseList(firstHalfEnd.Next)
    
    // 判断是否回文
    p1 := head
    p2 := secondHalfStart
    ans := true
    for ans && p2 != nil {
        if p1.Val != p2.Val {
            ans = false
        }
        p1 = p1.Next
        p2 = p2.Next
    }
    firstHalfEnd.Next = reverseList(secondHalfStart)
    return ans
}