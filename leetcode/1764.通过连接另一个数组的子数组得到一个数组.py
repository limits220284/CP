class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        k = 0
        for g in groups:
            while k + len(g) <= len(nums):
                if nums[k: k + len(g)] == g:
                    k += len(g)
                    break
                k += 1
            else:
                return False
        return True