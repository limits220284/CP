class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        a=s.count('1')
        b=target.count('1')
        n=len(s)
        if a!=0 and b==0:
            return False
        if a==0 and b!=0:
            return False
        return True