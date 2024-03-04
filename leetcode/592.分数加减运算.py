class Solution:
    def fractionAddition(self, expression: str) -> str:
        n=len(expression)
        ans=[[] for _ in range(2)]
        def gcd(a,b):
            return gcd(b,a%b) if b else a
        i=0
        while i<n:
            sign=1
            if expression[i]=='-' or expression[i]=='+':
                if expression[i]=='-':
                    sign=-1
                i+=1
            k=0
            while expression[i].isdigit():
                k+=1
                i+=1
            ans[0].append(sign*int(expression[i-k:i]))
            k=0
            i+=1
            while i<n and expression[i].isdigit():
                k+=1
                i+=1
            ans[1].append(int(expression[i-k:i]))
        #计算分母的最小公倍数
        a=prod(ans[1])
        b=sum(a/ans[1][i]*ans[0][i] for i in range(len(ans[1])))
        if b==0:
            return "0/1"
        c=gcd(a,abs(b))
        return str(int(b/c))+'/'+str(int(a/c))
                