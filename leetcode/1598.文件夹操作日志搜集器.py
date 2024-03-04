class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt=0
        for x in logs:
            if x=='../':
                if cnt==0:continue
                cnt-=1
            elif x=='./':
                continue
            else:
                cnt+=1
        return cnt if cnt>0 else 0
                
                
        