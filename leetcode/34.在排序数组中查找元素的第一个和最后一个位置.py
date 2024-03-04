class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找
        ans = []
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l == n or nums[l] != target:
            return [-1, -1]
        ans.append(l)
        l, r = 0, n-1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        ans.append(l)
        return ans