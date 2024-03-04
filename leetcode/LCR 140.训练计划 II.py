# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 快慢指针思想
        fast = head
        slow = head
        while k:
            fast = fast.next
            k -= 1
        while fast != None:
            slow = slow.next
            fast = fast.next
        return slow