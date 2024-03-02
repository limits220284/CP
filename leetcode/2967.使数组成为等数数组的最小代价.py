class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        def check(x):
            x = list(str(x))
            x_ = x[::]
            x_.reverse()
            if ''.join(x_) == ''.join(x):
                return True
            else:
                return False
        if n & 1:
            c = nums[n//2]
        else:
            c = (nums[n//2]+nums[n//2-1])//2
        m = len(str(c))
        m = m//2
        d = 10**m
        ans = 10**15
        p =-1
        for i in range((c//d-2)*d,(c//d+2)*d):
            if check(i) :
                ans = min(ans,sum(abs(nums[j]-i) for j in range(n)))
       
        
        return ans