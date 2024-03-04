class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        e=[0]*numCourses
        for x,y in prerequisites:
            g[y].append(x)
            e[x]+=1
        res=[]
        def topsort():
            que=deque()
            for i in range(numCourses):
                if e[i]==0:
                    que.append(i)
            while que:
                ans=que.popleft()
                res.append(ans)
                for x in g[ans]:
                    e[x]-=1
                    if e[x]==0:
                        que.append(x)
            return len(res)==numCourses
        if topsort():
            return res
        else:
            return []