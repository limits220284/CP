class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr=[[0]*(n+2) for _ in range(n+2)]
        def insert(x1,y1,x2,y2,c):
            arr[x1][y1]+=c
            arr[x2+1][y1]-=c
            arr[x1][y2+1]-=c
            arr[x2+1][y2+1]+=c
        q=len(queries)
        for i in range(q):
            x1,y1,x2,y2=queries[i]
            c=1
            insert(x1+1,y1+1,x2+1,y2+1,c)
        for i in range(1,n+1):
            for j in range(1,n+1):
                arr[i][j]+=arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]
        ans=[]
        for x in arr[1:-1]:
            ans.append(x[1:-1][::])
        return ans
