class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res=[]
        for x,y in queries:
            if x>y:
                x,y=y,x
            a,b=[],[]
            while x:
                a.append(x)
                x//=2
            while y:
                b.append(y)
                y//=2
            # 判断是否有相同的部分
            i=0
            n=min(len(a),len(b))
            a.reverse()
            b.reverse()
            while i<n:
                if a[i]==b[i]:
                    i+=1
                else:
                    break
            res.append(len(a)+len(b)-(2*i-1))
        return res
                
            
        