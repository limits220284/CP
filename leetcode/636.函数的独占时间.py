class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans=[0]*n
        stk=deque()
        cur=0
        for log in logs:
            id_2,soe_2,ti_2=log.split(':')
            id_2,ti_2=int(id_2),int(ti_2)
            if len(stk)==0:
                stk.append(log)
                cur=ti_2
            else:
                id_1,soe_1,ti_1=stk[-1].split(':')
                id_1,ti_1=int(id_1),int(ti_1)
                if soe_2=='start':
                    ans[id_1]+=ti_2-cur
                    cur=ti_2
                    stk.append(log)
                elif soe_2=='end':
                    stk.pop()
                    ans[id_2]+=ti_2-cur+1
                    cur=ti_2+1
        return ans