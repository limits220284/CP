# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l,r=None,None
        t=0
        cur=list1
        while cur:
            if t==a-1:
                l=cur
            if t==b+1:
                r=cur
            cur=cur.next
            t+=1
        l.next=list2
        while list2.next:
            list2=list2.next
        list2.next=r
        return list1