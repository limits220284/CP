class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res=-1
        cnt=Counter(nums)
        for x in cnt:
            if -x in cnt:
                res=max(res,abs(x))
        return res