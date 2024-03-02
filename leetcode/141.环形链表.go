func hasCycle(head *ListNode) bool {
    seen := map[*ListNode] int{}
    for head != nil{
        if _, ok := seen[head]; ok{
            return true
        }
        seen[head] += 1
        head = head.Next
    }
    return false
}
