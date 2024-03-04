class Solution:
    def solveEquation(self, equation: str) -> str:
        pre,nxt=equation.split('=')
        nm=0
        co=0
        def cnt(pre,sgn):
            nonlocal nm,co
            m=len(pre)
            i=0
            sign=1
            while i<m:
                if pre[i]=='+':
                    sign=1
                elif pre[i]=='-':
                    sign=-1
                else:
                    dig=''
                    while i<m and pre[i].isalnum():
                        dig+=pre[i]
                        i+=1
                    if dig[-1]=='x':
                        if len(dig)==1:
                            co+=sgn*sign
                        else:
                            co+=sgn*sign*int(dig[:-1])
                    else:
                        nm+=int(dig)*(-sign)*sgn
                    continue
                i+=1
        cnt(pre,1)
        cnt(nxt,-1)
        if co==0 and nm==0:
            return "Infinite solutions"
        if co==0 and nm:
            return "No solution"
        return "x="+str(int(nm//co))