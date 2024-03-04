class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # 最小的数匹配比它稍微大的数即可
        # 1 1 2 3 3 5
        # 1 1 2 3 3 5
        nums.sort()
        n = len(nums)
        i = 0
        ans = 0
        for x in nums:
            if x > nums[i]:
                i += 1
        return i