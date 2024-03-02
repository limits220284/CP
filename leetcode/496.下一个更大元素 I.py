class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stk = []
        for num in reversed(nums2):
            while stk and num > stk[-1]:
                stk.pop()
            res[num] = -1 if not stk else stk[-1]
            stk.append(num)
        return [res[num] for num in nums1]