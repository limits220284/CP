# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先反转链表
        head = self.reverseList(head)
        # print(head)
        # 复制链表
        root = ListNode(0)
        cur1 = root
        cur2 = head
        while cur2:
            new = ListNode(cur2.val)
            cur1.next = new
            cur1 = cur1.next
            cur2 = cur2.next
        # print(root.next)
        # 链表相加
        new = self.addTwoNumbers(head, root.next)
        # 反转链表
        new = self.reverseList(new)
        return new
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 节点值和进位加在一起
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
            if l1: l1 = l1.next  # 下一个节点
            if l2: l2 = l2.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre