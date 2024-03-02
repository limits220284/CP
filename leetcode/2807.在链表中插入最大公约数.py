# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 直接遍历
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)
        n = len(arr)
        if n == 0 or n == 1: return head
        ans = []
        for i in range(1, n):
            ans.append(arr[i-1])
            ans.append(gcd(arr[i-1], arr[i]))
        ans.append(arr[-1])
        print(ans)
        root = ListNode(0)
        cur = root
        for x in ans:
            Node = ListNode(x)
            cur.next = Node
            cur = cur.next
        return root.next
            
            
            