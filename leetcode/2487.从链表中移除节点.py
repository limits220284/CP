# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #通过单调找到右边第一个比其大的数
        cur=head
        stk=[]
        while cur:
            while stk and stk[-1].val<cur.val:
                stk.pop()
            stk.append(cur)
            cur=cur.next
        cur=stk[0]
        n=len(stk)
        for i in range(1,n):
            cur.next=stk[i]
            cur=cur.next
        return stk[0]
        