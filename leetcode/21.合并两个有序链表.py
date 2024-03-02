# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        res = ListNode(0)
        move = res
        while list1 and list2:
            if list1.val<=list2.val:
                move.next = list1
                list1 = list1.next
            else:
                move.next = list2
                list2 = list2.next
            move = move.next
        move.next = list1 if list1 else list2 # l1 或者 l2 尚未使用完，拼接到 结果链表 的最后
        return res.next

                

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # 创建哑节点作为 结果链表 的开头
#         dummy = ListNode(0)
#         # 有个游标，标识 结果链表 的结尾
#         move = dummy
#         # l1 和 l2 都未遍历结束
#         while l1 and l2:
#             # 如果 l1 的数值比较小
#             if l1.val <= l2.val:
#                 # 把 l1 头部节点拼接到 结果链表 的结尾
#                 move.next = l1
#                 # l1 指向下一个节点
#                 l1 = l1.next
#             else:
#                 # 把 l2 头部节点拼接到 结果链表 的结尾
#                 move.next = l2
#                 # l2 指向下一个节点
#                 l2 = l2.next
#             # 移动 结果链表 的结尾指针
#             move = move.next
#         # l1 或者 l2 尚未使用完，拼接到 结果链表 的最后
#         move.next = l1 if l1 else l2
#         # 返回哑节点的下一个位置
#         return dummy.next

