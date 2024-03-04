class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #相邻重复项，直接栈操作
        stk=[]
        for x in s:
            if stk and x==stk[-1][0]:
                stk[-1][1]+=1
                if stk[-1][1]==k:
                    stk.pop()
            else:
                stk.append([x,1])
        res=""
        for x in stk:
            res+=x[0]*x[1]
        return res