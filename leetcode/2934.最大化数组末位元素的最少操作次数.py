class Solution:
    def minOperations(self, arr1: List[int], arr2: List[int]) -> int:
        # 最后一位数不变
        n = len(arr1)
        def check(nums):
            for i in range(n - 2, -1, -1):
                if nums[i] > nums[-1]:
                    return False
            return True
        n = len(arr1)
        ans1 = 0
        nums1, nums2 = deepcopy(arr1), deepcopy(arr2)
        for i in range(n - 2, -1, -1):
            if nums1[i] <= nums1[-1]:
                continue
            else:
                nums1[i], nums2[i] = nums2[i], nums1[i]
                ans1 += 1
                if nums1[i] > nums1[-1]:
                    ans1 = inf
                    break
        if not check(nums2):
            ans1 = inf
        
        ans2 = 0
        nums1, nums2 = deepcopy(arr1), deepcopy(arr2)
        for i in range(n - 2, -1, -1):
            if nums2[i] <= nums2[-1]:
                continue
            else:
                nums2[i], nums1[i] = nums1[i], nums2[i]
                ans2 += 1
                if nums2[i] > nums2[-1]:
                    ans2 = inf
                    break
        if not check(nums1):
            ans2 = inf
        ans3 = 1
        nums1, nums2 = deepcopy(arr1), deepcopy(arr2)
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        for i in range(n - 2, -1, -1):
            if nums1[i] <= nums1[-1]:
                continue
            else:
                nums1[i], nums2[i] = nums2[i], nums1[i]
                ans3 += 1
                if nums1[i] > nums1[-1]:
                    ans3 = inf
                    break
        if not check(nums2):
            ans3 = inf
        ans4 = 1
        nums1, nums2 = deepcopy(arr1), deepcopy(arr2)
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        for i in range(n - 2, -1, -1):
            if nums2[i] <= nums2[-1]:
                continue
            else:
                nums1[i], nums2[i] = nums2[i], nums1[i]
                ans4 += 1
                if nums2[i] > nums2[-1]:
                    ans4 = inf
                    break
        if not check(nums1):
            ans4 = inf
        print(ans1, ans2, ans3, ans4)
        k = min(ans1, ans2, ans3, ans4)
        return -1 if k == inf else k