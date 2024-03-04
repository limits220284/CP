class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n=len(queries)
        m=len(pattern)
        res=[False for i in range(n)]
        for k,x in enumerate(queries):
            if len(x)<m:
                res[k]=False
            elif len(x)==m:
                if x==pattern:
                    res[k]=True
            else:
                i,j=0,0
                flag=True
                while j<len(x):
                    if i<m and x[j]==pattern[i]:
                        i+=1
                    else:
                        t=ord(x[j])-ord('a')
                        if t<0 or t>25:
                            flag=False
                            break
                    j+=1
                if flag and i==m:
                    res[k]=True
        return res