class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)
        p=list(itertools.permutations(range(1,n+2)))
        def is_valid(x):
            n=len(x)
            for i in range(1,n):
                if pattern[i-1]=='I':
                    if x[i]>x[i-1]:
                        continue
                    else:
                        return False
                elif pattern[i-1]=='D':
                    if x[i]<x[i-1]:
                        continue
                    else:
                        return False
            return True
        res="99999999"
        for x in p:
            if is_valid(x):
                res=min("".join(str(i) for i in x),res)
        return res