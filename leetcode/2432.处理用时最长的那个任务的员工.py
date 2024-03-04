class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        n=len(logs)
        mx=0
        _id=inf
        for i in range(n-1,0,-1):
            logs[i][1]-=logs[i-1][1]
        for x in logs:
            if x[1]>mx:
                mx=x[1]
                _id=x[0]
            elif x[1]==mx:
                _id=min(_id,x[0])
        return _id
        
            