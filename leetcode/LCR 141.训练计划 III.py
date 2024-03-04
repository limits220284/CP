# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 定义一个头节点
        if not head: return head
        root = ListNode(0, head)
        pre = None
        cur, nxt = head, head
        while nxt:
            nxt = nxt.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre