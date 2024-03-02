ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小

class Solution:
    def mergetwolist(self, a, b):
        cura, curb = a, b
        head = ListNode(0)
        cur = head
        while cura and curb:
            if cura.val < curb.val:
                cur.next = cura
                cura = cura.next
            else:
                cur.next = curb
                curb = curb.next
            cur = cur.next
        cur.next = cura if cura else curb
        return head.next
    def merge(self, lists, l, r):
        if l == r: return lists[l]
        if l > r: return None
        mid = (l + r) // 2
        return self.mergetwolist(self.merge(lists, l, mid), self.merge(lists, mid+1, r))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists) - 1)