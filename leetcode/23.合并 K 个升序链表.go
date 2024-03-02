/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    return merge(lists, 0, len(lists)-1)
}

func merge(lists []*ListNode, l, r int) *ListNode{
    if l == r {return lists[l]} 
    if l > r {return nil}
    mid := (l + r) / 2
    return mergetwolist(merge(lists, l, mid), merge(lists, mid + 1, r))
}

func mergetwolist(a, b *ListNode) *ListNode{
    if a == nil && b == nil{
        return nil
    }
    var head = &ListNode{}
    dummy := head
    for a != nil && b != nil{
        if a. Val < b.Val{
            head.Next = a
            a = a.Next
        }else{
            head.Next = b
            b = b.Next
        }
        head = head.Next
    }
    if a != nil{
        head.Next = a
    }else if b != nil{
        head.Next = b
    }
    return dummy.Next
}