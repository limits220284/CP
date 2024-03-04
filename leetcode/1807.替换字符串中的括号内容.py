class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        #栈
        ans=""
        stk=[]
        dic={}
        for x,y in knowledge:
            dic[x]=y
        for i,x in enumerate(s):
            if x!=')':
                stk.append(x)
            else:
                tmp=""
                while stk[-1]!="(":
                    tmp=stk.pop()+tmp
                stk.pop()
                if tmp in dic:
                    stk.append(dic[tmp])
                else:
                    stk.append("?")
        return "".join(stk)
            
        