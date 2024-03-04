class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        # 最小公倍数是几个数相乘然后除以最大公因数的数
        n=len(nums)
        cnt=0        
        for i in range(n):
            mul=nums[i]
            for j in range(i,n):
                d=gcd(mul,nums[j])
                mul=mul*nums[j]
                if mul//d==k:
                    cnt+=1
                mul//=d
        return cnt
                    
                    
                

                