# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head.next
        if fast == None:
            return False
        while fast != None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next
            if fast == None:
                return False
            fast = fast.next
        return False