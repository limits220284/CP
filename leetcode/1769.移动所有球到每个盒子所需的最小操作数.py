class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ansl=[0]*n
        cnt=0
        l=0
        for i in range(n):
            ansl[i]+=l*1+cnt
            if boxes[i]=='1':
                l+=1
            cnt=ansl[i]
        cnt=0
        r=0
        ansr=[0]*n
        for i in range(n-1,-1,-1):
            ansr[i]+=r*1+cnt 
            if boxes[i]=='1':
                r+=1
            cnt=ansr[i]
        return [x+y for x,y in zip(ansl,ansr)]        