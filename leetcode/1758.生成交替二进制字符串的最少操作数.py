class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        a,b=0,0
        for i in range(n):
            if i%2==0:
                a+=int(s[i])
            else:
                b+=int(s[i])
        # 返回有两种情况，一种是偶数位0变成1，奇数位置1变成0
        # 另外一种是偶数位置1变成0，奇数位置0变成1
        return min((n+1)//2-a+b,a+n//2-b)
        