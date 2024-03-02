class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = [0, 0]
        for x in nums1:
            if cnt2[x]:
                ans[0] += 1
        for x in nums2:
            if cnt1[x]:
                ans[1] += 1
        return ans