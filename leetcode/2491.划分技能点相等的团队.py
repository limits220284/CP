class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot=sum(skill)
        n=len(skill)
        one=tot//(n//2)
        i,j=0,n-1
        while i<j:
            if skill[i]+skill[j]!=one:
                return -1
            i+=1
            j-=1
        res=0
        i,j=0,n-1
        while i<j:
            res+=skill[i]*skill[j]
            i+=1
            j-=1
        return res