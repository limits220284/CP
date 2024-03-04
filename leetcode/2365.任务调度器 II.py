class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        dic={}
        dp=[]
        n=len(tasks)
        cnt=0
        for i in range(n):
            if dic.get(tasks[i]) is not None:
                pre=dic[tasks[i]]
                if cnt-pre-1<space:
                    ans=space-(cnt-pre-1)
                    print(ans)
                    cnt+=ans
            cnt+=1
            dic[tasks[i]]=cnt-1
        return cnt