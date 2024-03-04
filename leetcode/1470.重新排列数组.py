class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        res=[]
        i=0
        while i<n//2:
            res.append(nums[i])
            res.append(nums[i+n//2])
            i+=1
        return res
            