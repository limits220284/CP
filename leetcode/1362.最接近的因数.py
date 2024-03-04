class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        div=num+1 if num==1 else num+2
        i=int(sqrt(div))
        while div%i>1:
            i-=1
        return [i,div//i]