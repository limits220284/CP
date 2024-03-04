class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            mx=nums[i]
            for j in range(i,n):
                mx=gcd(mx,nums[j])
                if mx==k:
                    cnt+=1
                elif mx<k:
                    break
        return cnt
                    
                    
                