class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        dic1=Counter(nums1)
        dic2=Counter(nums2)
        for x in nums1:
            if x in dic1 and x in dic2:
                return x
        return -1