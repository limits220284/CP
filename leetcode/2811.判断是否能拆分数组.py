class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # 只要存在两个相邻的数和大于m就可以，如果不行就返回false
        if len(nums) <= 2: return True
        for x, y in pairwise(nums):
            if x + y >= m:
                return True
        return False
        
            
            