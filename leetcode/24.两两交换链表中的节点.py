# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # o(n)做法
        root = ListNode(0)
        root.next = head
        cur, pre= head, root
        while cur and cur.next:
            nxt = cur.next
            tmp = nxt.next
            nxt.next = cur
            cur.next = tmp
            pre.next = nxt
            pre = cur
            cur = tmp
        return root.next