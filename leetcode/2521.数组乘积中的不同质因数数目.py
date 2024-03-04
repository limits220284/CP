class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        dic=Counter()
        def divide(x):
            up=int(math.sqrt(x))+1
            for i in range(2,up):
                #此时i一定是一个质数,如果这里不是质数,则代表存在小于i的质因子,但是上一步已经将i-1内的质因子都除去了
                if x%i==0:
                    while x%i==0:
                        x//=i
                        dic[i]+=1
            if x>1:
                dic[x]+=1
        for a in nums:
            divide(a)
        return len(dic)
