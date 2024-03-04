# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root=ListNode(0,head)
        cur=root.next
        pre=root
        while cur:
            if cur.val==val:
                cur=cur.next
                del pre.next
                pre.next=cur
            else:
                cur=cur.next
                pre=pre.next
        return root.next
                