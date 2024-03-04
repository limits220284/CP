class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 广度优先搜索
        gr=[[] for i in range(n)]
        gb=[[] for i in range(n)]
        for x,y in redEdges:
            gr[x].append(y)
        for x,y in blueEdges:
            gb[x].append(y)
        ans=[-1]*n
        def bfs(f):
            s=set()
            vis=[False]*n
            que=deque([[0,f]])
            dep=0
            vis[0]=True
            while que:
                m=len(que)
                dep+=1
                for i in range(m):
                    t,color=que.popleft()
                    if color=='b':
                        for c in gr[t]:
                            if ans[c]==-1:
                                ans[c]=dep
                            else:
                                ans[c]=min(ans[c],dep)
                            if (t,c,'r') not in s:
                                que.append([c,'r'])
                                s.add((t,c,'r'))
                    else:
                        for c in gb[t]:
                            if ans[c]==-1:
                                ans[c]=dep
                            else:
                                ans[c]=min(ans[c],dep)
                            if (t,c,'b') not in s:
                                que.append([c,'b'])
                                s.add((t,c,'b'))
        ans[0]=0
        bfs('r')
        bfs('b')
        return ans

