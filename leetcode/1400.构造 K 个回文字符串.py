class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n=len(s)
        if n<k:return False
        if n==k:return True
        dic=Counter(s)
        a=0
        for x in dic.values():
            if x%2==1:
                a+=1
        if a>k:
            return False
        return True
            