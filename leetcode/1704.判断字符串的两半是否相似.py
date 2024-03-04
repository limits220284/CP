class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        y_s='aeiouAEIOU'
        dic=Counter([x for x in y_s])
        n=len(s)
        a,b=0,0
        for i in range(n//2):
            if s[i] in dic:
                a+=1
            if s[n//2+i] in dic:
                b+=1
        return a==b