class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        k=0
        cnt=0
        for i,x in enumerate(nums):
            if x==0:
                k+=1
            else:
                cnt+=k*(k+1)//2
                k=0
        cnt+=k*(k+1)//2
        return cnt