class Solution:
    def smallestValue(self, n: int) -> int:
        #循环直到为质数停止即可
        def divide(x):
            #返回质因子之和即可
            res=0
            up=int(math.sqrt(x))+1
            for i in range(2,up):
                #此时i一定是一个质数,如果这里不是质数,则代表存在小于i的质因子,但是上一步已经将i-1内的质因子都除去了
                s=0
                if x%i==0:
                    while x%i==0:
                        x//=i
                        s+=1
                    res+=i*s
            if x>1:
                res+=x
            # print(res)
            return res
        cnt=n
        while True:
            x=divide(n)
            cnt=min(cnt,x)
            if x==n:
                break
            else:
                n=x
        return cnt
                
        