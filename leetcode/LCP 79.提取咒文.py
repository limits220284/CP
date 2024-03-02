class Solution:
    def extractMantra(self, matrix: List[str], mantra: str) -> int:
        ma = []
        mantra = list(mantra)
        vis = []
        for c in matrix:
            ma.append(list(c))
            vis.append([0]*len(c))
        # print(ma)
        n = len(ma)
        m = len(ma[0])
        h = deque()        
        h.append([0,0,0,0])
        vis[0][0]=1
        def check(x,y):
            return x >= 0 and y >= 0 and x < n and y < m
        fx = [[0,1],[0,-1],[1,0],[-1,0]]
        while len(h) > 0:
            #print(h)
            v = h.popleft()
            #print(v)            
            #print(vis)
            if ma[v[0]][v[1]] == mantra[v[2]]:
                #print(mantra[v[2]])
                if v[2] == len(mantra)-1:
                    return v[3]+1
                h.append([v[0],v[1],v[2]+1,v[3]+1])
                continue
            for f in fx:
                xx = v[0]+f[0]
                yy = v[1]+f[1]
                if check(xx,yy) and vis[xx][yy] <= v[2]:  
                    if ma[xx][yy] == mantra[v[2]]:
                        if v[2] == len(mantra)-1:
                            return v[3]+2
                        h.append([xx,yy,v[2]+1,v[3]+2])
                    else:
                        h.append([xx,yy,v[2],v[3]+1]) 
                    vis[xx][yy] += 1
        return -1