class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n=len(grades)
        i=1
        while True:
            if i*(i+1)//2==n:
                return i
            elif i*(i+1)//2>n:
                break
            i+=1
        return i-1