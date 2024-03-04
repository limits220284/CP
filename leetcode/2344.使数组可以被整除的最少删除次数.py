class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a,b):
            if a==0 or b==0:
                return a if a else b
            if a==1 or b==1:
                return a if a==1 else b
            if a<b:
                a,b=b,a
            return gcd(b,a%b)
        for i in range(len(numsDivide)-1):
            k=gcd(numsDivide[i],numsDivide[i+1])
            numsDivide[i+1]=k
        mf=numsDivide[len(numsDivide)-1]
        nums.sort()
        for i in range(len(nums)):
            if mf%nums[i]==0:
                return i
        return -1
            