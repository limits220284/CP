class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        s = list(accumulate(nums, initial = 0))
        ans = []
        n = len(nums)
        for q in queries:
            # l = bisect_left(nums, q)
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= q:
                    r = mid
                else:
                    l = mid + 1
            ans.append(l * q - s[l] + s[-1] - s[l] - (n-l) * q)
        return ans
        