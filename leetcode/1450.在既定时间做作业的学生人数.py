class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n=len(startTime)
        cnt=0
        for x,y in zip(startTime,endTime):
            if queryTime<=y and queryTime>=x:
                cnt+=1
        return cnt