class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numsSet = set(nums)
        inSet = False
        res = 0
        while head:
            if head.val not in numsSet:
                inSet = False
            elif not inSet:
                inSet = True
                res += 1
            head = head.next
        return res