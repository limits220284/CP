#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def FindMiddleNode(self, head:Optional[ListNode]) -> ListNode:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverseListNode(self, head:Optional[ListNode]) -> ListNode:
        pre, cur = None, head
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 找到中间节点
        mid = self.FindMiddleNode(head)
        # 反转链表, mid之后的链表反转了
        head2 = self.reverseListNode(mid)
        # 重排链表
        while head2.next != None:
            t1 = head.next
            t2 = head2.next
            head.next = head2
            head2.next = t1
            head = t1
            head2 = t2



