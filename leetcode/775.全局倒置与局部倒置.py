class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        #差分数组可以求解多少个数大于当前的这个数，但是空间复杂度为O(n)
        #主要思想是，在[0,n-1]中如果出现比当前数大的数，就在该数之前的位置上都加一，然后下次遍历到该数的时候，就可以知道在这之前有多少数大于当前该数了，然后进行相加即可得到总的全局倒置
        n=len(nums)
        for i in range(n):
            if abs(nums[i]-i)>1:
                return False
        return True