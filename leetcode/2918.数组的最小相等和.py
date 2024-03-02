class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cnt01 = nums1.count(0)
        cnt02 = nums2.count(0)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if cnt01 and cnt02:
            return max(sum1 + cnt01, sum2 + cnt02)
        if cnt01:
            if sum1 >= sum2:
                return -1
            elif sum1 < sum2:
                if sum2 - sum1 >= cnt01:
                    return sum2
                elif sum2 - sum1 < cnt01:
                    return -1
        if cnt02:
            if sum2 >= sum1:
                return -1
            elif sum2 < sum1:
                if sum1 - sum2 >= cnt02:
                    return sum1
                elif sum1 - sum2 < cnt02:
                    return -1
        if sum1 == sum2:
            return sum1
        return -1