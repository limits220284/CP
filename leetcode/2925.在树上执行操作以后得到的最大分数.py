class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        tot = sum(values)
        dic = defaultdict(list)
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])
        vis = set()
        
        def dfs(v):
            
            vis.add(v)
            
            score = 0
            for u in dic[v]:
                if u in vis:
                    continue
                score+=dfs(u)
            return min(score,values[v]) if score != 0 else values[v]
            
        return tot-dfs(0)
            