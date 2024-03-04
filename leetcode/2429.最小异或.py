class Solution:
    def minimizeXor(self, x: int, y: int) -> int:
        num1,num2=x,y
        arr1=[0]*32
        arr2=[0]*32
        i=31
        while i:
            arr1[i]=num1&1
            arr2[i]=num2&1
            num1>>=1
            num2>>=1
            i-=1
        t1=bin(x).count('1')
        t2=bin(y).count('1')
        if t1>=t2:
            sub=t1-t2
            for i in range(31,-1,-1):
                if arr1[i]==1 and sub:
                    arr1[i]=0
                    sub-=1
                    if sub==0:break
        else:
            sub=t2-t1
            for i in range(31,-1,-1):
                if arr1[i]==0 and sub:
                    arr1[i]=1
                    sub-=1
                    if sub==0:break
        # print(arr1)
        ans=0
        for i in range(31,-1,-1):
            ans+=arr1[i]*2**(31-i)
        return ans
                
                