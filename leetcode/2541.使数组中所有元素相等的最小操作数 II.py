class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if sum(nums1)!=sum(nums2):
            return -1
        if k==0 and nums1!=nums2:
            return -1
        if k==0:
            return 0
        dis=[x-y for x,y in zip(nums1,nums2)]
        #3 0 -6 3
        ans=0
        for x in dis:
            if x%k!=0:
                return -1
            elif x>0:
                ans+=x//k
        return ans