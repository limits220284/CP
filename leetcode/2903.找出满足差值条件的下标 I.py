class Solution:
    def findIndices(self, nums: List[int], idf: int, vdf: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if j - i >= idf and abs(nums[i] - nums[j]) >= vdf:
                    return [i, j]
        return [-1, -1]