class Solution:
    def removeStars(self, s: str) -> str:
        #栈操作
        stk=[]
        for c in s:
            if c!='*':
                stk.append(c)
            else:
                stk.pop()
        return "".join(stk)