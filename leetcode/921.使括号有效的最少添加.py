class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt=0
        res=0
        for x in s:
            if x=='(':
                cnt+=1
            elif x==')' and cnt==0:
                res+=1
            else:
                cnt-=1
        return res+cnt
        # stk=[]
        # cnt=0
        # i=0
        # n=len(s)
        # while i<n:
        #     if s[i]=='(':
        #         stk.append(s[i])
        #     elif s[i]==')':
        #         if stk:
        #             stk.pop()
        #         else:
        #             cnt+=1
        #     i+=1
        # return cnt+len(stk)
                
        