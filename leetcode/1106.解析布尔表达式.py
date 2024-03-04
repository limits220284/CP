class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # 使用栈进行模拟即可
        stk=[]
        for x in expression:
            if len(stk)==0 or x=='(' or x=='!' or x=='&' or x=='|':
                stk.append(x)
            elif x=='t' or x=='f':
                stk.append(True if x=='t' else False) 
            elif x==')':
                t,f=0,0
                while stk[-1]!='(':
                    if stk.pop():
                        t+=1
                    else:
                        f+=1
                # 弹出(
                stk.pop()
                # 弹出 运算符
                op=stk.pop()
                if op=='!':
                    stk.append(True if f==1 else False)
                elif op=='|':
                    stk.append(True if t else False)
                elif op=='&':
                    stk.append(False if f else True)
        return stk[-1]